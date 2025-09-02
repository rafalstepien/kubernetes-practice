from fastapi import FastAPI
import uvicorn
import os
import logging
from pydantic import BaseModel

logger = logging.getLogger(__name__)
app = FastAPI()



class Numbers(BaseModel):
    numbers: list[int]
    
    
@app.post("/add")
async def info(numbers: Numbers):
    return {"answer": str(sum(numbers.numbers))}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=os.environ.get("CALCULATOR_BACKEND_PORT"))


