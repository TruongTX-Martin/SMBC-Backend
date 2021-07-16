import os

from ...mocks.repositories import MockStorageRepository
import unittest

from app.services import StorageService
from app.services.storages import S3, Local


class TestStorageService(unittest.TestCase):
    def setup_method(self, _method):
        pass

    def teardown_method(self, _method):
        pass

    @staticmethod
    def _get_service():
        return StorageService(local_storage=Local(), s3_storage=S3())
