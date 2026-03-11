from fastapi import APIRouter, Depends, status, Path
from sqlalchemy.orm import Session
from server.src.data.database import get_db
from server.src.sales.schemas.sales_schema import SaleCreate
from server.src.sales.services.sales_service import SalesService
from server.src.common.messages.common_messages import CommonMessages

router = APIRouter(prefix="/sales", tags=["Sales"])


@router.post(
    "/",
    summary="Create a new sale",
    description="Create a new sale with the provided details.",
    status_code=status.HTTP_201_CREATED,
    responses={
        201: {
            "description": "Created",
            "content": {
                "application/json": {
                    "example": {
                        "id": 1,
                        "created_at": "2026-03-09T18:09:43.449145",
                        "total": 9.99,
                        "status": "completed",
                    }
                }
            },
        },
        400: {"description": CommonMessages.BAD_REQUEST},
        422: {"description": CommonMessages.UNPROCESSABLE_ENTITY},
    },
)
def create_sale(data: SaleCreate, db: Session = Depends(get_db)):
    new_sale = SalesService.new_sale(data, db)
    return new_sale


@router.get(
    "/",
    summary="List all sales",
    description="List all sales.",
    responses={
        200: {
            "description": "OK",
            "content": {
                "application/json": {
                    "example": [
                        {
                            "id": 1,
                            "created_at": "2026-02-23T19:31:06.267635",
                            "total": 9.99,
                            "status": "completed",
                        }
                    ]
                }
            },
        },
        404: {"description": CommonMessages.NOT_FOUND},
    },
)
def list_sales(db: Session = Depends(get_db)):
    return SalesService.get_sales(db)


@router.get(
    "/{id}",
    summary="Get a sale by ID",
    description="Retrieve a sale by its unique ID.",
    responses={
        200: {
            "description": "OK",
            "content": {
                "application/json": {
                    "example": {
                        "id": 1,
                        "created_at": "2026-02-23T19:31:06.267635",
                        "total": 9.99,
                        "status": "completed",
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
    return SalesService.get_sale_by_id(db, id)
