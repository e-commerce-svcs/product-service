import starlite

from app.db import events as db_events


def get_start_app_handler():
    async def start_app(state: starlite.State) -> None:
        await db_events.create_db_engine(state)
        await db_events.create_db_tables(state)

    return start_app


def get_stop_app_handler():
    async def stop_app(state: starlite.State) -> None:
        await db_events.dispose_db_engine(state)

    return stop_app
