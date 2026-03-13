from fastapi import APIRouter, Depends, Path, status
from sqlalchemy.orm import Session
from server.src.data.database import get_db
from server.src.products.messages.product_messages import ProductMessages
from server.src.products.schemas.product_schema import (
    ProductCreate,
    ProductResponse,
    ProductUpdate,
)
from server.src.products.services.product_service import ProductService
from server.src.common.messages.common_messages import CommonMessages

router = APIRouter(prefix="/products", tags=["Products"])


@router.post(
    "/",
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
                        "active": True,
                    }
                }
            },
        },
        400: {"description": CommonMessages.BAD_REQUEST},
        409: {"description": CommonMessages.CONFLICT},
        422: {"description": CommonMessages.UNPROCESSABLE_ENTITY},
    },
)
def create_product(data: ProductCreate, db: Session = Depends(get_db)):
    new_product = ProductService.create_new_product(db, data)
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
                            "active": True,
                        }
                    ]
                }
            },
        },
        404: {"description": CommonMessages.NOT_FOUND},
    },
)
def list_all_products(db: Session = Depends(get_db)):
    return ProductService.list_products(db)


@router.get("/search")
def search_products_by_name(name: str, db: Session = Depends(get_db)):
    products = ProductService.search_products_by_name(db, name)
    return products


@router.get(
    "/{id}",
    summary="Get a product by ID",
    description="Retrieve a product by its unique ID.",
    response_model=ProductResponse,
    responses={
        200: {
            "description": "OK",
            "content": {
                "application/json": {
                    "example": {
                        "id": 1,
                        "name": "Example Product",
                        "price": 9.99,
                        "stock": 100,
                        "barcode": "1234567890123",
                        "active": True,
                    }
                }
            },
        },
        404: {"description": CommonMessages.NOT_FOUND},
        422: {"description": CommonMessages.UNPROCESSABLE_ENTITY},
    },
)
def get_by_id(
    id: int = Path(..., ge=1, le=2_147_483_647), db: Session = Depends(get_db)
):
    product = ProductService.get_product(db, id)

    return product


@router.patch(
    "/{id}",
    summary="Update a product",
    description="Update an existing product with new details.",
    response_model=ProductResponse,
    responses={
        200: {
            "description": "OK",
            "content": {
                "application/json": {
                    "example": {
                        "id": 1,
                        "name": ProductMessages.PRODUCT_UPDATED,
                        "price": 19.99,
                        "stock": 50,
                        "barcode": "1234567890123",
                        "active": True,
                    }
                }
            },
        },
        404: {"description": CommonMessages.NOT_FOUND},
        422: {"description": CommonMessages.UNPROCESSABLE_ENTITY},
    },
)
def put_product(
    id: int = Path(..., ge=1, le=2_147_483_647),
    data: ProductUpdate = ...,
    db: Session = Depends(get_db),
):
    updated_product = ProductService.update_product(db, id, data)
    return updated_product
