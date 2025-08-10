from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Order Service", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "order-service"}

@app.get("/orders/{user_id}")
async def get_orders(user_id: int):
    return {"user_id": user_id, "orders": []}

@app.post("/orders")
async def create_order():
    return {"message": "Create order endpoint"}

@app.get("/orders/{order_id}")
async def get_order(order_id: int):
    return {"order_id": order_id}