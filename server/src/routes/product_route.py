from fastapi import APIRouter, Depends, Path, status
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


@router.post(
    "/create",
    summary="Create a new product",
    description="Create a new product with the provided details.",
    response_model=ProductResponse,
    status_code=status.HTTP_201_CREATED,
    responses={
        201: {
            "description": "Created",
            "content": {
                "application/json": {
                    "example": {
                        "id": 1,
                        "name": "Example Product",
                        "price": 9.99,
                        "stock": 100,
                        "barcode": "1234567890123",
                    }
                }
            },
        },
        400: {"description": "Bad Request"},
        409: {"description": "Conflict - Product already exists"},
    },
)
def create_product(data: ProductCreate, db: Session = Depends(get_db)):
    new_product = create_new_product(db, data)
    return new_product


@router.get(
    "/",
    summary="List all products",
    description="Retrieve a list of all products.",
    response_model=list[ProductResponse],
    status_code=status.HTTP_200_OK,
    responses={
        200: {
            "description": "OK",
            "content": {
                "application/json": {
                    "example": [
                        {
                            "id": 1,
                            "name": "Example Product",
                            "price": 9.99,
                            "stock": 100,
                            "barcode": "1234567890123",
                        }
                    ]
                }
            },
        },
        404: {"description": "Not Found - No products available"},
    },
)
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
