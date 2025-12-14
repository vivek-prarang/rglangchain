from fastapi import FastAPI
from app.routers import auth_router


app = FastAPI(
    title="Post Man API Tester",
    description="",
    version="0.0.1",
    docs_url="/documentation",
)
app.include_router(
    auth_router, 
    prefix="/auth", 
    tags=["Auth"],
    dependencies=[],
    )

