import starlite
from sqlalchemy.ext.asyncio import engine

from app.db.repositories import products


async def get_db_engine(state: starlite.State) -> engine.AsyncEngine:
    if isinstance(state.engine, engine.AsyncEngine):
        return state.engine

    raise TypeError(
        "sqlalchemy.ext.asyncio.engine.AsyncEngine is missing from starlite.State"
    )


async def get_products_repo(state: starlite.State) -> products.ProductsRepository:
    if isinstance(state.repositories, dict):
        products_repo: products.ProductsRepository = state.repositories["products"]
        return products_repo

    raise TypeError("dict is missing from starlite.State")
