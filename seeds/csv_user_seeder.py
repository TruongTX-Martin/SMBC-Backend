from app.models import User

from .csv_seeder import CsvSeeder


class CsvUserSeeder(CsvSeeder):
    model_class = User
    require_truncate = True
    buck_insert = True

    def _generate_data(self):
        data = self._read_csv('users.csv')
        return data
