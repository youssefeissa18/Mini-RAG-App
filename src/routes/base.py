from fastapi import FastAPI, APIRouter
import os
from helpers.config import get_settings
base_router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1"],
    

)

@base_router.get("/")
async def welcome_message():
    apps_settings = get_settings()
    appname = apps_settings.APP_NAME
    appversion = apps_settings.APP_VERSION

    return {
        "message": f"Welcome to {appname} version {appversion}! This application allows you to upload files and interact with them using a simple API."
        } 