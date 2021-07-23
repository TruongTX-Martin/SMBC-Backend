from app.models import User

from .base_seeder import BaseSeeder


class UserSeeder(BaseSeeder):
    base_model = User

    @staticmethod
    def _generate_data():
        return [{
            'id': 1,
            'email': 'admin@example.com',
            'password': 'testtest',
        }]
