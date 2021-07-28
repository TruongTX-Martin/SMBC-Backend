## How to use cache


## How to use?

Call transaction context in your code
```python
from app.cache import cache

@app.route('', methods=["GET"])
@cache.cached(timeout=Config.CACHE_TIMEOUT_SECONDS, query_string=True)
@inject
def get_setting_using_cache():
```

## Usage document

https://flask-caching.readthedocs.io/en/latest/

## Detail design of transaction

- [cache/__init__.py](../app/cache/__init__.py)
