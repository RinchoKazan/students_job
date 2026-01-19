from pydantic import BaseModel, Field, ConfigDict


class ProductBase(BaseModel):
    name: str = Field(..., min_length=1)
    description: str
    price: int


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class ProductUpdatePartial(ProductBase):
    name: str | None = None
    description: str | None = None
    price: int | None = None


class Product(ProductBase):
    # model_config = ConfigDict(from_attributes=True)
    class Config:
        from_attributes = True

    id: int
