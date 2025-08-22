from fastapi import FastAPI
import uvicorn
import logging
import httpx
import os
from pydantic import BaseModel

logger = logging.getLogger(__name__)
app = FastAPI()


class Numbers(BaseModel):
    numbers: list[int]


@app.post("/add")
async def info(numbers: Numbers):
    async with httpx.AsyncClient() as client:
        backend_port = os.environ.get("CALCULATOR_BACKEND_PORT")
        r = await client.post(
            url=f"http://dev-calculator-backend-service:{backend_port}/add",
            json=numbers.model_dump()
        )
    return r.json()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("CALCULATOR_API_PORT")))


