from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel, Field

import data_interactor as di



class Contact(BaseModel):
    id: int = Field(..., alias= id)
    first_name: str = Field(..., max_length=50)
    last_name: str = Field(..., max_length=50)
    phone_number: str = Field(..., max_length=20)

    def to_dict(self):
        return {
                "first_name": self.first_name, 
                "last_name": self.last_name, 
                "phone_number": self.phone_number
                }

app = FastAPI()
mongodb = di.MongodbInstance()
mongodb.get_database()



@app.get("/contacts")
def get_all_contacts():
    return mongodb.select()

@app.post("/contacts")
def post_new_contact(contact: Contact):
    return mongodb.insert(contact)

@app.update("/contacts/{id}")
def update_contact():
    pass

@app.delete("/contacts/{id}")
def delete_contact(id: int):
    pass

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
