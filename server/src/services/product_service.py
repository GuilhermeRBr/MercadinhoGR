from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from server.src.models.product_model import Product
from server.src.schemas.product_schema import ProductResponse


def create_new_product(db: Session, data):
    new_product = Product(**data.model_dump())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return ProductResponse.model_validate(new_product)


def list_products(db: Session):
    products = db.query(Product).all()
    if not products:
        return []
    return [ProductResponse.model_validate(product) for product in products]


def get_product(db: Session, product_id: int):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
        )
    return ProductResponse.model_validate(product)


def update_product(db: Session, product_id: int, data):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
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
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
        )
    db.delete(product)
    db.commit()
