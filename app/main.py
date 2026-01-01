from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth_router
from app.config.settings import settings


app = FastAPI(
    title=settings.app_name,
    description="",
    version=settings.app_version,
    docs_url="/docx",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    auth_router, 
    prefix="/auth", 
    tags=["Auth"],
    dependencies=[],
    )

