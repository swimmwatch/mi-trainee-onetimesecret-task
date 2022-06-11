"""
Advert service routers
"""
from fastapi import APIRouter

from services.onetimesecret.routers import secret

api_router = APIRouter()
api_router.include_router(secret.router)
