from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session
from server.src.data.database import get_db
from server.src.schemas.product_schema import ProductCreate, ProductResponse
from server.src.services.product_service import (
    create_new_product,
    get_product,
    list_products,
    update_product,
    delete_product,
)

router = APIRouter(prefix="/products", tags=["products"])


@router.post("/", response_model=ProductResponse)
def create_product(data: ProductCreate, db: Session = Depends(get_db)):
    new_product = create_new_product(db, data)
    return new_product


@router.get("/", response_model=list[ProductResponse])
def list_all_products(db: Session = Depends(get_db)):
    return list_products(db)


@router.get("/{product_id}", response_model=ProductResponse)
def get_by_id(
    product_id: int = Path(..., ge=1, le=2_147_483_647), db: Session = Depends(get_db)
):
    product = get_product(db, product_id)

    return product


@router.put("/{product_id}", response_model=ProductResponse)
def put_product(
    product_id: int = Path(..., ge=1, le=2_147_483_647),
    data: ProductCreate = ...,
    db: Session = Depends(get_db),
):
    updated_product = update_product(db, product_id, data)
    return updated_product


@router.delete("/{product_id}")
def del_product(
    product_id: int = Path(..., ge=1, le=2_147_483_647), db: Session = Depends(get_db)
):
    delete_product(db, product_id)
    return {"detail": "Product deleted successfully"}
