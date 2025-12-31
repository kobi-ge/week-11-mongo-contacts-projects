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

# creating an instance of mongodb connection
mongodb = di.MongodbInstance()
mongodb.get_database()


@app.get("/contacts")
def get_all_contacts():
    """
    Docstring for get_all_contacts
    this function uses the select method from MongodbInstance to read from DB
    """
    return mongodb.select()

@app.post("/contacts")
def post_new_contact(contact: Contact):
    """
    Docstring for post_new_contact
    
    :param contact: new contact information
    :type contact: Contact class (base model)
    """
    result = mongodb.insert(contact)
    return{
            "message": "Contact created successfully",
            "id": str(result.inserted_id)
        }

@app.put("/contacts/{id}")
def update_contact(contact: Contact, id):
    try:
        contact = contact.to_dict()
        query = { '$set': contact } 
        modified_count = mongodb.update(id, query)   
        if modified_count > 0:
            return {"message": "Contact updated successfully"}        
        return {"message": "Contact not found or no changes made"}
    except HTTPException as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.delete("/contacts/{id}")
def delete_contact(id):
    try:
        deleted_count = mongodb.delete(id)
        if deleted_count > 0:
            return {"message": "Contact deleted successfully"}
        return {"message": "Contact not found"}
    except HTTPException as e:
        raise HTTPException(status_code=404, detail=str(e))

