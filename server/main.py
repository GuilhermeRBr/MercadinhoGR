from fastapi import FastAPI
from server.src.data.database import engine, Base
from server.src.routes.product_route import router as product_router

app = FastAPI()
API_PREFIX = "/api"

Base.metadata.create_all(bind=engine)
app.include_router(product_router, prefix=API_PREFIX)
print("Server is running... http://localhost:8000")

# running with uvicorn server.main:app --reload
# runnig on http://localhost:8000
