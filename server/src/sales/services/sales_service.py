from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from server.src.products.models.product_model import Product
from server.src.sales.models.sales_model import Sale, SaleItem
from server.src.sales.schemas.sales_schema import SaleCreate


class SalesService:
    @staticmethod
    def new_sale(data: SaleCreate, db: Session):
        if not data.items:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="A venda deve conter pelo menos um item.",
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
                        status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Produto com ID {item.product_id} não encontrado.",
                    )

                if product.stock < item.quantity:
                    raise HTTPException(
                        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                        detail=f"Estoque insuficiente para o produto {product.name}.",
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
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e)
            )

    def get_sales(db: Session):
        sales = db.query(Sale).all()
        if not sales:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Nenhuma venda encontrada"
            )
        return sales
