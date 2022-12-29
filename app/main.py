import starlite

from app.core import config, events


def get_application():
    start_app = events.get_start_app_handler()
    stop_app = events.get_stop_app_handler()
    cors_config = starlite.CORSConfig(allow_origins=config.settings.ALLOW_ORIGINS)

    return starlite.Starlite(
        route_handlers=[],
        on_shutdown=[stop_app],
        on_startup=[
            start_app,
        ],
        cors_config=cors_config,
        debug=config.settings.DEBUG,
    )


app = get_application()
