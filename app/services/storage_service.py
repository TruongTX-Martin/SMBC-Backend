from pathlib import Path
from typing import List

from app.config import Config
from app.services.storages import S3, Local


class StorageService(object):
    def __init__(self, s3_storage: S3, local_storage: Local, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._s3_storage = s3_storage
        self._local_storage = local_storage
        self._storage = None

    def upload_file(self,
                    path: Path,
                    media_type: str,
                    parent_dirs: List = None) -> str:
        return self.storage().create_file(path, media_type, parent_dirs)

    def get_temp_url(self, key: str) -> str:
        return self.storage().get_url(key)

    def storage(self):
        if not self._storage:
            if Config.STORAGE_TYPE == 's3':
                self._storage = self._s3_storage
            else:
                self._storage = self._local_storage

        return self._storage
