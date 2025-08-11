from fastapi import FastAPI
import uvicorn
import os
import logging


logger = logging.getLogger(__name__)
app = FastAPI()

ENGINE_VERSION = "0.2.0"
ENGINE_APP_PORT = "8080"

@app.get("/version")
async def info():
    return {"ENGINE_VERSION": ENGINE_VERSION}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=ENGINE_APP_PORT)


