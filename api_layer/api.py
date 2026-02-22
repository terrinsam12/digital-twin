from fastapi import FastAPI
from api_layer.twin_api import router

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Digital Twin API running"}

app.include_router(router)