from pydantic import BaseModel, Field
from typing import List


class SaleItemCreate(BaseModel):
    product_id: int = Field(gt=0, example=1, le=1_000_000)
    quantity: int = Field(gt=0, example=1, le=1_000_000)


class SaleCreate(BaseModel):
    items: List[SaleItemCreate] = Field(min_length=1)
