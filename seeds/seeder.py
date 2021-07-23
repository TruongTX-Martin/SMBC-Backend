import os

from .user_seeder import UserSeeder


class Seeder:
    def __init__(self, db):
        self.db = db

    def execute(self):
        if os.getenv('FLASK_ENV') == 'development':
            UserSeeder(db=self.db).execute()
