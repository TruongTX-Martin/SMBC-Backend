import codecs
import logging
import sys

from flask import jsonify, url_for
from flask._compat import text_type
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
import sadisplay

from app import models
from app.bootstrap import create_app
from app.config import Config
from app.database import db


class TextColor:
    HEADER = '\033[95m'
    SUCCESS = '\033[92m'
    WARNING = '\033[93m'
    IMPORTANT = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'


class MyManager(Manager):
    def run(self, commands=None, default_command=None):
        """
        Prepares manager to receive command line input. Usually run
        inside "if __name__ == "__main__" block in a Python script.

        :param commands: optional dict of commands. Appended to any commands
                         added using add_command().

        :param default_command: name of default command to run if no
                                arguments passed.
        """

        if Config.FLASK_ENV not in ['test', 'development']:
            self._echo(
                "Executing command on {} environment.".format(
                    Config.FLASK_ENV.upper()), TextColor.IMPORTANT)

            environment = input("Input environment name to continue? ").lower()
            if environment != Config.FLASK_ENV:
                self._echo("Environment name not correct. Exit.",
                           TextColor.IMPORTANT)
                sys.exit(1)

        if commands:
            self._commands.update(commands)

        # Make sure all of this is Unicode
        argv = list(text_type(arg) for arg in sys.argv)
        if default_command is not None and len(argv) == 1:
            argv.append(default_command)

        try:
            result = self.handle(argv[0], argv[1:])
        except SystemExit as e:
            result = e.code

        sys.exit(result or 0)

    @staticmethod
    def _echo(msg, level=TextColor.ENDC):
        print(f"{level} {msg} {TextColor.ENDC}")


app = create_app()
app.logger.setLevel(logging.INFO)
migrate = Migrate(app, db)
manager = MyManager(app)
manager.add_command('database', MigrateCommand)


@manager.command
def run():
    app.run(host=Config.APP_HOST, port=Config.APP_PORT)  #5000


@manager.command
def list_routes():
    import urllib
    output = []
    for rule in app.url_map.iter_rules():

        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        line = urllib.parse.unquote("{:50s} {:20s} {}".format(
            rule.endpoint, methods, url))
        output.append(line)

    for line in sorted(output):
        print(line)


@manager.command
def seed():
    """Add seed data to the database."""
    print('Loading fixtures.')

    from seeds.seeder import Seeder
    Seeder(db=db).execute()

    db.session.commit()
    print('Done.')


@manager.command
def generate_erd():
    desc = sadisplay.describe([getattr(models, attr) for attr in dir(models)])
    with codecs.open('documents/db/schema.plantuml', 'w',
                     encoding='utf-8') as f:
        f.write(sadisplay.plantuml(desc))
    with codecs.open('documents/db/schema.dot', 'w', encoding='utf-8') as f:
        f.write(sadisplay.dot(desc))


@manager.command
@manager.option('-p', '--path', dest='path')
def test(path="tests"):
    """Runs the tests."""
    if Config.FLASK_ENV != 'test':
        print('Only run test on test environment')
        sys.exit(1)

    if path is None:
        path = "tests"
    pytest.main(["-s", path])


if __name__ == '__main__':
    manager.run()
