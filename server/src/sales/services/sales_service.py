from fastapi import HTTPException
from sqlalchemy.orm import Session
from server.src.products.models.product_model import Product
from server.src.sales.models.sales_model import Sale, SaleItem
from server.src.sales.schemas.sales_schema import SaleCreate
from server.src.sales.messages.sales_messages import SALES_MESSAGES


class SalesService:
    @staticmethod
    def new_sale(data: SaleCreate, db: Session):
        if not data.items:
            raise HTTPException(
                status_code=422,
                detail=SALES_MESSAGES.INVALID_SALE,
            )

        new_sale = Sale(total=0, status="pending")
        db.add(new_sale)
        db.flush()

        total = 0

        try:
            for item in data.items:

                product = (
                    db.query(Product).filter(Product.id == item.product_id).first()
                )

                if not product:
                    raise HTTPException(
                        status_code=404,
                        detail=SALES_MESSAGES.PRODUCT_NOT_FOUND,
                    )

                if product.stock < item.quantity:
                    raise HTTPException(
                        status_code=400,
                        detail=SALES_MESSAGES.STOCK_NOT_ENOUGH + product.name,
                    )
                if product.active is False:
                    raise HTTPException(
                        status_code=400,
                        detail=SALES_MESSAGES.PRODUCT_NOT_ACTIVE,
                    )

                subtotal = product.price * item.quantity
                total += subtotal

                product.stock -= item.quantity

                sales_item = SaleItem(
                    sale_id=new_sale.id,
                    product_id=item.product_id,
                    quantity=item.quantity,
                    price=product.price,
                )

                db.add(sales_item)

            new_sale.total = total
            new_sale.status = "completed"

            db.commit()
            db.refresh

            db.refresh(new_sale)
            return new_sale

        except Exception as e:
            new_sale.status = "canceled"
            db.commit()
            raise e

    @staticmethod
    def get_sales(db: Session):
        sales = db.query(Sale).all()
        if not sales:
            raise HTTPException(status_code=404, detail=SALES_MESSAGES.SALES_NOT_FOUND)
        return sales

    @staticmethod
    def get_sale_by_id(db: Session, sale_id: int):
        sale = db.query(Sale).filter(Sale.id == sale_id).first()
        if not sale:
            raise HTTPException(status_code=404, detail=SALES_MESSAGES.SALE_NOT_FOUND)
        return sale
