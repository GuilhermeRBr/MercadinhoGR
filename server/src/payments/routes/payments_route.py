from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from server.src.core.dependency import get_current_user
from server.src.data.database import get_db
from server.src.payments.schema.payments_schema import PaymentCreate, PaymentResponse
from server.src.payments.services.payments_service import PaymentService
from server.src.common.messages.common_messages import CommonMessages

router = APIRouter(prefix="/payments", tags=["Payments"])


@router.post(
    "/",
    summary="Create a new payment",
    description="Record a new payment for a specific sale.",
    status_code=status.HTTP_201_CREATED,
    response_model=PaymentResponse,
    responses={
        400: {"description": CommonMessages.BAD_REQUEST},
        401: {"description": CommonMessages.UNAUTHORIZED},
        404: {"description": CommonMessages.NOT_FOUND},
        422: {"description": CommonMessages.UNPROCESSABLE_ENTITY},
    },
)
def create_payment(
    data: PaymentCreate,
    _: str = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    new_payment = PaymentService.create_payment(data, db)
    return new_payment
