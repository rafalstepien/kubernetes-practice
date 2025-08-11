from fastapi import FastAPI
import uvicorn
import os
import requests
import logging


logger = logging.getLogger(__name__)
app = FastAPI()

API_ENVIRONMENT = os.getenv("API_ENVIRONMENT") or ""
API_PORT = int(os.getenv("API_PORT"))
ENGINE_SERVICE_PORT = os.getenv("ENGINE_SERVICE_PORT")
ENGINE_SERVICE_BASE_URL = os.getenv("ENGINE_SERVICE_BASE_URL")
API_VERSION = "0.11.0"
ENGINE_SERVICE_FULL_URL = f"http://{ENGINE_SERVICE_BASE_URL}:{ENGINE_SERVICE_PORT}/version"

logger.info(f"API_PORT: {str(API_PORT)}")

@app.get("/")
async def root():
    return {"message": "root"}


@app.get("/info")
async def info():
    return {"API_ENVIRONMENT": API_ENVIRONMENT, "API_VERSION": API_VERSION, "ENGINE_SERVICE_FULL_URL": ENGINE_SERVICE_FULL_URL}


@app.get("/engine_version")
async def get_engine_version():
    r = requests.get(ENGINE_SERVICE_FULL_URL)
    return r.json()



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=API_PORT)


