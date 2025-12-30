from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel, Field

import data_interactor as di



class Contact(BaseModel):
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
    result = mongodb.insert(contact)
    return{
            "message": "Contact created successfully",
            "id": str(result.inserted_id)
        }

@app.put("/contacts/{id}")
def update_contact(contact: Contact, id):
    contact = contact.to_dict()
    query = { '$set': contact } 
    modified_count = mongodb.update(id, query)   
    if modified_count > 0:
        return {"message": "Contact updated successfully"}
    
    return {"message": "Contact not found or no changes made"}

@app.delete("/contacts/{id}")
def delete_contact(id):
    deleted_count = mongodb.delete(id)
    if deleted_count > 0:
        return {"message": "Contact deleted successfully"}
    return {"message": "Contact not found"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000)
