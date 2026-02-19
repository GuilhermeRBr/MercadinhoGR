from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from server.src.products.models.product_model import Product
from server.src.products.schemas.product_schema import ProductResponse
from server.src.products.messages.product_messages import ProductMessages


def create_new_product(db: Session, data):
    if (
        db.query(Product).filter(Product.barcode == data.barcode).first()
        or db.query(Product).filter(Product.name == data.name).first()
    ):
        raise HTTPException(
            status_code=409, detail=ProductMessages.PRODUCT_ALREADY_EXISTS
        )
    elif data.stock <= 0:
        raise HTTPException(status_code=422, detail=ProductMessages.INVALID_STOCK)
    elif data.price <= 0:
        raise HTTPException(status_code=422, detail=ProductMessages.INVALID_PRICE)

    new_product = Product(**data.model_dump())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return ProductResponse.model_validate(new_product)


def list_products(db: Session):
    products = db.query(Product).all()
    if not products:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=ProductMessages.NO_PRODUCTS_FOUND,
        )
    return [ProductResponse.model_validate(product) for product in products]


def get_product(db: Session, product_id: int):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=ProductMessages.PRODUCT_NOT_FOUND,
        )
    return ProductResponse.model_validate(product)


def update_product(db: Session, product_id: int, data):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=ProductMessages.PRODUCT_NOT_FOUND,
        )
    for key, value in data.model_dump().items():
        setattr(product, key, value)
    db.commit()
    db.refresh(product)
    return ProductResponse.model_validate(product)


def delete_product(db: Session, product_id: int):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=ProductMessages.PRODUCT_NOT_FOUND,
        )
    db.delete(product)
    db.commit()
