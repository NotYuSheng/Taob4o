from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Product Service", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "product-service"}

@app.get("/products")
async def get_products():
    return {"products": []}

@app.get("/products/{product_id}")
async def get_product(product_id: int):
    return {"product_id": product_id}

@app.post("/products")
async def create_product():
    return {"message": "Create product endpoint"}