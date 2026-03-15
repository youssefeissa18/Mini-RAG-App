from fastapi import FastAPI, File, UploadFile

from routes import base

app = FastAPI()

app.include_router(base.base_router)