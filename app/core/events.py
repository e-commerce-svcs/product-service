import starlite


def get_start_app_handler():
    async def start_app(state: starlite.State) -> None:
        ...

    return start_app


def get_stop_app_handler():
    async def stop_app(state: starlite.State) -> None:
        ...

    return stop_app
