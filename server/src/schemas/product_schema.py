from typing import Optional
from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    price: float
    stock: int
    category_id: int
    supplier_id: int
    barcode: Optional[str] = None

class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    stock: int
    category_id: int
    supplier_id: int
    barcode: str

    class Config:
        from_attributes = True