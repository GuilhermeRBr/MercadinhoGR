from pydantic import BaseModel, Field
from typing import List


class SaleItemCreate(BaseModel):
    product_id: int
    quantity: int = Field(gt=0)


class SaleCreate(BaseModel):
    items: List[SaleItemCreate] = Field(min_length=1)
