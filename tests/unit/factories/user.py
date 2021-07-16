from datetime import datetime

from faker import Faker
from faker.providers import internet

from app.database import db
from app.models import User
import factory

fake = Faker()
fake.add_provider(internet)


class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = 'commit'

    password = factory.Sequence(lambda n: "test_password-{}".format(n))
    email = fake.email()

    created_at = datetime.now()
    updated_at = datetime.now()
