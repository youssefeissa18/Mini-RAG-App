from fastapi import FastAPI, APIRouter
import os
base_router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1"],
    

)

@base_router.get("/")
async def welcome_message():
    appname = os.getenv("APP_NAME")
    appversion = os.getenv("APP_VERSION")

    return {
        "message": f"Welcome to {appname} version {appversion}! This application allows you to upload files and interact with them using a simple API."
        } 