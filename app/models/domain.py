import pydantic


class Product(pydantic.BaseModel):
    id: int
    name: str
    description: str
    price: float
    image: pydantic.AnyHttpUrl
    tags: list[str]
