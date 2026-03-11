from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.get("/welcome")
def welcome_message():
    return {
        "message": "Welcome to the Mini RAG App! This application allows you to upload files and interact with them using a simple API."
    }