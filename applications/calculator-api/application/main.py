from fastapi import FastAPI
import uvicorn
import logging
import requests
import os

logger = logging.getLogger(__name__)
app = FastAPI()


@app.get("/add/")
async def info(
    number_1: int,
    number_2: int
):
    r = requests.get(f"http://calculator-backend-service/?number_1={number_1}?&number_2={number_2}")
    return r.json()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=os.environ.get("CALCULATOR_API_PORT"))


