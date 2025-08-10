from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Cart Service", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "cart-service"}

@app.get("/cart/{user_id}")
async def get_cart(user_id: int):
    return {"user_id": user_id, "items": []}

@app.post("/cart/{user_id}/items")
async def add_to_cart(user_id: int):
    return {"message": "Add to cart endpoint"}

@app.delete("/cart/{user_id}/items/{item_id}")
async def remove_from_cart(user_id: int, item_id: int):
    return {"message": "Remove from cart endpoint"}