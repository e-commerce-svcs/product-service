import pydantic
import sqlmodel
import starlite
from sqlalchemy.ext import asyncio as sa_asyncio

from app.core import config
from app.db.repositories import products


async def create_db_engine(state: starlite.State):
    assert isinstance(config.settings.DATABASE_URL, pydantic.PostgresDsn)
    database_url = config.settings.DATABASE_URL.replace(
        "postgres://", "postgresql+asyncpg://"
    )
    state.engine = sa_asyncio.create_async_engine(
        database_url, **config.settings.sqlalchemy_kwargs
    )


async def dispose_db_engine(state: starlite.State) -> None:
    await state.engine.dispose()


async def init_db_repositories(state: starlite.State) -> None:
    state.repositories = {
        "products": products.ProductsRepository(),
    }


async def create_db_tables(state: starlite.State) -> None:
    engine = state.engine

    if isinstance(engine, sa_asyncio.engine.AsyncEngine):
        async with engine.begin() as conn:
            await conn.run_sync(sqlmodel.SQLModel.metadata.create_all)
    else:
        raise TypeError(
            "sqlalchemy.ext.asyncio.engine.AsyncEngine is missing from starlite.State"
        )
