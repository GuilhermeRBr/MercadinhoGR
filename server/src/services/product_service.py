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