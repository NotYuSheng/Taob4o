from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Inventory Service", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "inventory-service"}

@app.get("/inventory/{product_id}")
async def get_inventory(product_id: int):
    return {"product_id": product_id, "quantity": 100}

@app.put("/inventory/{product_id}")
async def update_inventory(product_id: int):
    return {"message": "Update inventory endpoint"}