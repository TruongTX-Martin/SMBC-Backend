<<<<<<< HEAD
import os
from faker import Faker
from werkzeug.datastructures import FileStorage

from app.services import StorageService
from app.services.storage import Local, S3, BaseStorage

from ...mocks.repositories import MockStorageRepository
import unittest
=======
import unittest

from app.services import StorageService
from app.services.storages import S3, Local
>>>>>>> 92d3f91... improve model setting


class TestStorageService(unittest.TestCase):
    def setup_method(self, _method):
        pass

    def teardown_method(self, _method):
        pass

<<<<<<< HEAD
    def test_upload(self):
        service = self._get_service()

        path = os.getcwd()
        fileTmp = open(path+"/tests/unit/mocks/test_data/image.jpg", "rb")

        file = FileStorage(fileTmp)
        fileObject = service.upload(file)
        assert fileObject.url is not None

    @staticmethod
    def _get_service():
        return StorageService(MockStorageRepository(None), Local(), S3())
=======
    @staticmethod
    def _get_service():
        return StorageService(local_storage=Local(), s3_storage=S3())
>>>>>>> 92d3f91... improve model setting
