from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel

class ContactSchema(BaseModel):
    first_name: str
    last_name: str
    phone_number: str

app = FastAPI()

@app.get("/")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
