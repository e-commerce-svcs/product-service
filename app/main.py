import starlite
from starlite.cache import redis_cache_backend

from app.core import config, events


def get_application():
    start_app = events.get_start_app_handler()
    stop_app = events.get_stop_app_handler()
    cors_config = starlite.CORSConfig(allow_origins=config.settings.ALLOW_ORIGINS)
    redis_config = redis_cache_backend.RedisCacheBackendConfig(
        url=config.settings.REDIS_URL,
        port=6379,
        db=0,
        password=None,
    )
    redis_backend = redis_cache_backend.RedisCacheBackend(config=redis_config)

    return starlite.Starlite(
        route_handlers=[],
        on_shutdown=[stop_app],
        on_startup=[
            start_app,
        ],
        cors_config=cors_config,
        debug=config.settings.DEBUG,
        cache_config=starlite.CacheConfig(backend=redis_backend),
    )


app = get_application()
