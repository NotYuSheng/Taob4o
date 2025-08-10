from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="User Service", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "user-service"}

@app.get("/users")
async def get_users():
    return {"users": []}

@app.post("/users/register")
async def register_user():
    return {"message": "User registration endpoint"}

@app.post("/users/login")
async def login_user():
    return {"message": "User login endpoint"}