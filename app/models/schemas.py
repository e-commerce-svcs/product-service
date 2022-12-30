import pydantic
import sqlmodel


class Products(sqlmodel.SQLModel, table=True):
    id: pydantic.UUID4 | None = sqlmodel.Field(default=None, primary_key=True)  # type: ignore
    name: str
    description: str
    price: float
    image: str
    tags: list[str] = []
