from fastapi import FastAPI
import uvicorn
import os
import logging


logger = logging.getLogger(__name__)
app = FastAPI()


@app.get("/add/")
async def info(
    number_1: int,
    number_2: int
):
    return {"answer": str(number_1 + number_2)}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=os.environ.get("CALCULATOR_BACKEND_PORT"))


