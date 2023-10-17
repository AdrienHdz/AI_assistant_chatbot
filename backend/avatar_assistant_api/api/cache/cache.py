from api.app_settings import AppSettings
from cashews import cache, Cache as CacheConfigurator  # noqa: F401


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


is_cache_enabled = True
caching_module = initialize_caching(AppSettings())
ROUTE_CACHING = caching_module
