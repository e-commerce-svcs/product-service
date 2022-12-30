import starlite
from pydantic import UUID4

from app.models import domain


class ProductController(starlite.Controller):
    path = "/products"

    @starlite.get()
    async def index(self) -> list[domain.Product]:
        ...

    @starlite.post()
    async def create(self, data: domain.Product) -> domain.Product:
        ...

    @starlite.patch(path="/{user_id:uuid}")
    async def partial_update(
        self, user_id: UUID4, data: starlite.Partial[domain.Product]
    ) -> domain.Product:
        ...

    @starlite.put(path="/{user_id:uuid}")
    async def update(self, user_id: UUID4, data: domain.Product) -> domain.Product:
        ...

    @starlite.get(path="/{user_id:uuid}")
    async def show(self, user_id: UUID4) -> domain.Product:
        ...

    @starlite.delete(path="/{user_id:uuid}")
    async def delete(self, user_id: UUID4) -> None:
        ...
