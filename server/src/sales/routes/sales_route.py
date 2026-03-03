from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from server.src.data.database import get_db
from server.src.sales.schemas.sales_schema import SaleCreate
from server.src.sales.services.sales_service import SalesService

router = APIRouter(prefix="/sales", tags=["Sales"])


@router.post(
    "/create",
    summary="Create a new sale",
    description="Create a new sale with the provided details.",
    status_code=status.HTTP_201_CREATED,
    responses={
        201: {"description": "Created"},
        400: {"description": "Bad Request"},
        422: {"description": "Unprocessable Entity"},
    },
)
def create_sale(data: SaleCreate, db: Session = Depends(get_db)):
    new_sale = SalesService.new_sale(data, db)
    return new_sale


@router.get(
    "/list",
    summary="List all sales",
    description="List all sales.",
    responses={
        200: {"description": "OK"},
        404: {"description": "Not Found"},
        422: {"description": "Unprocessable Entity"},
    },
)
def list_sales(db: Session = Depends(get_db)):
    return SalesService.get_sales(db)
