from fastapi import FastAPI
import uvicorn
import logging
import os

logger = logging.getLogger(__name__)
app = FastAPI()


@app.get("/")
async def info():
    return {
        "APP_NAME": "info-microservice", 
        "APP_VERSION": "x.y.z", 
        "APP_STATUS": "operating"
    }



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("INFO_BACKEND_PORT")))


