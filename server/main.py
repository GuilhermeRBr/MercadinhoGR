from fastapi import FastAPI
from server.src.common.exceptions import validation_exception_handler
from fastapi.exceptions import RequestValidationError
from server.src.data.database import engine, Base
from server.src.products.routes.product_route import router as product_router
from server.src.sales.routes.sales_route import router as sales_router
from server.src.user.routes.user_route import router as user_router

app = FastAPI(
    title="Mercadinho GR",
    description="API para gerenciamento de produtos e vendas em um Mercadinho GR",
    version="1.0.0",
)
API_PREFIX = "/api"

app.add_exception_handler(RequestValidationError, validation_exception_handler)

Base.metadata.create_all(bind=engine)
app.include_router(product_router, prefix=API_PREFIX)
app.include_router(sales_router, prefix=API_PREFIX)
app.include_router(user_router, prefix=API_PREFIX)
print("Server is running... http://localhost:8000")

# running with uvicorn server.main:app --reload
# runnig on http://localhost:8000
