from flask import Flask

from flask_caching import Cache

from ..config import Config

cache = Cache(config={
    'CACHE_TYPE': Config.CACHE_TYPE,
    'CACHE_DIR': Config.CACHE_DIR
})


def init_cache(app: Flask):
    cache.init_app(app)
