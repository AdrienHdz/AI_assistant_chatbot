import importlib

from api.app_settings import AppSettings


def default_function(*args, **options):
    def decorator(fn):
        return fn

    return decorator


caching_module = None
is_cache_enabled = False
ROUTE_CACHING = None


def initialize_caching(AppSettings):
    host = AppSettings.host
    port = AppSettings.redis_port
    cache_instance = CacheConfigurator()
    params = {
        "socket_timeout": 0.5,
    }
    connection_string = f"{host}://{host}:{port}"
    cache_instance.setup(connection_string, **params)
    return cache_instance


try:
    caching_module = importlib.import_module("cashews").cache
    CacheConfigurator = importlib.import_module("cashews").Cache
    is_cache_enabled = True

except ImportError:
    caching_module = default_function

else:
    caching_module = initialize_caching(AppSettings())

ROUTE_CACHING = caching_module
