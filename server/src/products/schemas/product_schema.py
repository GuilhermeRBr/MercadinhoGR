from typing import Optional
from pydantic import BaseModel, Field


class ProductCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=100, example="Coca-Cola 2L")
    price: float = Field(..., gt=0, example=9.99)
    stock: int = Field(..., ge=0, example=100, le=1_000_000)
    barcode: Optional[str] = Field(
        None, min_length=8, max_length=13, example="1234567890123"
    )


class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    stock: int
    barcode: str

    class Config:
        from_attributes = True
