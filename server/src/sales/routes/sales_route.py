from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from server.src.data.database import get_db
from server.src.sales.schemas.sales_schema import SaleCreate
from server.src.sales.services.sales_service import new_sale

router = APIRouter(prefix="/sales", tags=["Sales"])


@router.post(
    "/create",
    summary="Create a new sale",
    description="Create a new sale with the provided details.",
)
def create_sale(data: SaleCreate, db: Session = Depends(get_db)):
    return new_sale(data, db)
