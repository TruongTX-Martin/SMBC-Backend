from faker import Faker

from app.bootstrap import create_app
from app.config import Config
from app.database import db


class BaseTestBase:
    db = None
    app_context = None

    @classmethod
    def setup_class(cls):
        app = create_app()
        cls.app = app
        cls.mock = cls.app.test_client(cls)
        cls.app_context = cls.app.app_context()
        cls.db = db

        cls.faker = Faker()

        with cls.app_context:
            # only migrate database in test environment
            if Config.FLASK_ENV == 'test':
                cls.db.create_all()
        cls.app_context.push()

    @classmethod
    def teardown_class(cls):
        with cls.app_context:
            # only migrate database in test environment
            if Config.FLASK_ENV == 'test':
                cls.db.session.remove()
                cls.db.drop_all()
        cls.app_context.pop()
