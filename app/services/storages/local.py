from pathlib import Path
import shutil
from typing import List

from flask import url_for

from ...config import Config
from .base import Base


class Local(Base):
    def create_file(self,
                    path: Path,
                    media_type: str,
                    parent_dirs: List = None) -> str:
        key = self._generate_key(path.name)

        destination = Config.STORAGE_LOCAL_DIRECTORY + '/' + key
        shutil.copy(str(path.resolve()), destination)

        return key

    def get_url(self, key: str) -> str:
        return url_for('static', filename='data/' + key)
