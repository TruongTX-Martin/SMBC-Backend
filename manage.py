from datetime import datetime
import urllib.parse

from flask import jsonify, url_for
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
import pytest

from app.bootstrap import create_app
from app.config import Config
from app.database import db

app = create_app()
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('database', MigrateCommand)


@manager.command
def run():
    app.run(host=Config.APP_HOST, port=Config.APP_PORT)


@manager.command
def test():
    """Runs the tests."""
    pytest.main(["-s", "tests"])


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
def cluster_poll_user():
    """Run analysis service to cluster users of poll"""

    start_time = datetime.now()
    print('Started executing grouping user start_time = %s.' % start_time)

    from app.repositories import PollRepository, PollUserGroupRepository, StatementPollUserGroupRepository,\
        UserPollRepository, StatementRepository, VoteRepository
    from app.services import AnalysisService
    poll_user_group_repository = PollUserGroupRepository(database=db)
    statement_poll_user_group_repository = StatementPollUserGroupRepository(
        database=db)
    statement_repository = StatementRepository(database=db)
    vote_repository = VoteRepository(database=db)
    poll_repository = PollRepository(database=db)
    user_poll_repository = UserPollRepository(database=db)
    analysis_service = AnalysisService(
        statement_repository=statement_repository,
        vote_repository=vote_repository,
        poll_user_group_repository=poll_user_group_repository,
        statement_poll_user_group_repository=
        statement_poll_user_group_repository,
        user_poll_repository=user_poll_repository,
        poll_repository=poll_repository)

    analysis_service.execute_grouping()

    duration = datetime.now() - start_time
    print("--- duration = %s seconds ---" % duration.seconds)


if __name__ == '__main__':
    manager.run()
