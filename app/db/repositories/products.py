import typing

import sqlmodel
from sqlalchemy.engine import result as sqlalchemy_result
from sqlalchemy.ext import asyncio as sqlalchemy_asyncio
from sqlmodel.engine import result
from sqlmodel.ext.asyncio import session
from sqlmodel.sql import expression

from app.core import abc


class ProductsRepository(abc.Database):
    """Database implementation for the products table."""

    def __init__(self) -> None:
        # Avoid an SAWarning. See: https://github.com/tiangolo/sqlmodel/issues/189
        expression.SelectOfScalar.inherit_cache = True  # type: ignore
        expression.Select.inherit_cache = True  # type: ignore

    async def add(
        self, engine: sqlalchemy_asyncio.AsyncEngine, table_model: sqlmodel.SQLModel
    ) -> None:
        async with session.AsyncSession(engine) as async_session:
            async_session.add(table_model)
            await async_session.commit()

    async def delete(
        self,
        engine: sqlalchemy_asyncio.AsyncEngine,
        table_model: sqlmodel.SQLModel,
        attribute: str,
    ) -> None:
        _ = engine
        _ = table_model
        _ = attribute

        raise NotImplementedError

    async def select(
        self,
        engine: sqlalchemy_asyncio.AsyncEngine,
        table_model: sqlmodel.SQLModel,
        attribute: str,
        query: str,
    ) -> result.ScalarResult[typing.Any]:
        model = type(table_model)

        async with session.AsyncSession(engine) as async_session:
            # Temp ignore incompatible type passed to `exec()`. See:
            # https://github.com/tiangolo/sqlmodel/issues/54
            # https://github.com/tiangolo/sqlmodel/pull/58
            row: result.ScalarResult[typing.Any] = await async_session.exec(
                sqlmodel.select(model).where(  # type: ignore
                    getattr(model, attribute) == query
                )
            )

        return row

    async def select_all(
        self, engine: sqlalchemy_asyncio.AsyncEngine, table_model: sqlmodel.SQLModel
    ) -> result.ScalarResult[typing.Any]:
        _ = engine
        _ = table_model

        raise NotImplementedError

    async def select_join(
        self,
        engine: sqlalchemy_asyncio.AsyncEngine,
        main_model: sqlmodel.SQLModel,
        *table_models: type[sqlmodel.SQLModel],
    ) -> result.ScalarResult[typing.Any]:
        _ = engine
        _ = main_model
        _ = table_models

        raise NotImplementedError

    async def select_all_join(
        self,
        engine: sqlalchemy_asyncio.AsyncEngine,
        *table_models: type[sqlmodel.SQLModel] | sqlmodel.SQLModel,
    ) -> sqlalchemy_result.ChunkedIteratorResult:
        _ = engine
        _ = table_models

        raise NotImplementedError

    async def update(
        self,
        engine: sqlalchemy_asyncio.AsyncEngine,
        table_model: sqlmodel.SQLModel,
        attribute: str,
    ) -> None:
        _ = engine
        _ = table_model
        _ = attribute

        raise NotImplementedError
