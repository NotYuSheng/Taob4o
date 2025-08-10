from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Payment Service", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "payment-service"}

@app.post("/payments")
async def process_payment():
    return {"message": "Process payment endpoint"}

@app.get("/payments/{payment_id}")
async def get_payment(payment_id: int):
    return {"payment_id": payment_id}