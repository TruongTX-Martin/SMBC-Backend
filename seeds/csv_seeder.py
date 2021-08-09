from csv import DictReader
import os
from pathlib import Path

from .base_seeder import BaseSeeder


class CsvSeeder(BaseSeeder):
    @staticmethod
    def _read_csv(filename: str):
        dir_path = str(Path(__file__).resolve().parent)
        file_path = os.path.join(dir_path, 'data', filename)
        with open(file_path, 'r') as read_obj:
            dict_reader = DictReader(read_obj)
            list_of_dict = list(dict_reader)
            return list_of_dict
