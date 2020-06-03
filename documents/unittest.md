# How to run unittest

`docker-compose exec app  poetry run python manage.py test`

`poetry run python manage.py test`

## 1. Service unittest

You can find service unittest under 
`app-dir/tests/unit/app/services/`

```python
class TestStorageService:
    def setup_method(self, _method):
        pass

    def teardown_method(self, _method):
        pass

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
```

### If service required repository, you should create Mock repository
The mock repository should be under

`app-dir/tests/unit/mocks/repositories/`