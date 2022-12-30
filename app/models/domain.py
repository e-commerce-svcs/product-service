import pydantic


class Product(pydantic.BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int
