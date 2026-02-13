from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from server.src.data.database import get_db
from server.src.schemas.product_schema import ProductCreate, ProductResponse
from server.src.services.product_service import create_new_product, list_products


router = APIRouter(prefix="/products", tags=["products"])

@router.post("/", response_model=ProductResponse)
def create_product(data: ProductCreate, db: Session = Depends(get_db)):
    new_product = create_new_product(db, data)
    return new_product

@router.get("/", response_model=list[ProductResponse])
def list_all_products(db: Session = Depends(get_db)):
    return list_products(db)