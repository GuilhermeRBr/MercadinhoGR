from fastapi import FastAPI
from server.src.common.exceptions import validation_exception_handler
from fastapi.exceptions import RequestValidationError
from server.src.data.database import engine, Base
from server.src.products.routes.product_route import (
    router as product_router,
)
from server.src.sales.routes.sales_route import router as sales_router
from server.src.user.routes.user_route import router as user_router
from server.src.login.routes.login_route import router as login_router
from server.src.payments.routes.payments_route import router as payments_router
from server.src.seed.seed_admin import seed_admin
from server.src.data.database import SessionLocal

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Mercadinho GR",
    description="API para gerenciamento de produtos e vendas no Mercadinho GR",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_PREFIX = "/api"

app.add_exception_handler(
    RequestValidationError, validation_exception_handler
)

Base.metadata.create_all(bind=engine)
app.include_router(product_router, prefix=API_PREFIX)
app.include_router(sales_router, prefix=API_PREFIX)
app.include_router(user_router, prefix=API_PREFIX)
app.include_router(login_router, prefix=API_PREFIX)
app.include_router(payments_router, prefix=API_PREFIX)


@app.on_event("startup")
def startup():
    db = SessionLocal()
    seed_admin(db)


print("Server is running... http://localhost:8000")

# running with uvicorn server.main:app --reload
# runnig on http://localhost:8000
