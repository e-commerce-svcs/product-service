import pydantic

from app.models import domain


class ProductService:
    async def index(self):
        ...

    async def create(self, data: domain.Product):
        ...

    async def partial_update(self, user_id: pydantic.UUID4, data: domain.Product):
        ...

    async def update(self, user_id: pydantic.UUID4, data: domain.Product):
        ...

    async def show(self, user_id: pydantic.UUID4):
        ...

    async def delete(self, user_id: pydantic.UUID4):
        ...
