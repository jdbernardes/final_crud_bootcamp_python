from pydantic import BaseModel, PositiveFloat, EmailStr

# from enum import Enum
from datetime import datetime
from typing import Optional

# The reason why I am creating 3 versions is because depending on
# the type of operation I am performing some fields may be needed
# but in other operations they may not, for example:
# when creating a product is not needed to provide ID and created at
# since they are auto generated, now in query they are part of.


class ProductBase(BaseModel):
    name: str
    description: str
    price: PositiveFloat
    category: str
    suplier_email: EmailStr


class ProductCreate(ProductBase):
    pass


class ProducResponse(ProductBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class ProductUpdate(ProductBase):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[PositiveFloat] = None
    category: Optional[str] = None
    suplier_email: Optional[EmailStr] = None
