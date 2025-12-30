from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import os
from dotenv import load_dotenv
from bson import ObjectId

load_dotenv()

HOST = os.getenv("MONGO_HOST")
PORT = int(os.getenv("MONGO_PORT"))
DB = os.getenv("MONGO_DB")

class MongodbInstance:
    def __init__(self):
        self.db =None
        self.collection = None

    def get_database(self):
        try:
            client = MongoClient(f"mongodb://{HOST}:{PORT}")
            client.admin.command("ping")
            self.db = client[DB]
            self.collection = self.db.contacts
            return "Successfully connected to MongoDB"
        
        except ConnectionFailure as e:
            return f"failed to connect to db: {e}"


    def select(self, id = None):
        if self.db is None:
            self.get_database()
        contact_list = []
        for doc in self.collection.find():
            doc['id'] = str(doc['_id'])
            del doc['_id']
            contact_list.append(doc)
        return contact_list

    def insert(self, contact):
        contact = contact.to_dict()
        result = self.db.contacts.insert_one(contact)
        return result
         
    def update(self, id, query):
        query_filter = {'_id': ObjectId(id)}
        result = self.collection.update_one(query_filter, query)
        return result.modified_count

    def delete(self, id):
        query_filter = {'_id': ObjectId(id)}
        result =  self.collection.delete_one(query_filter)
        return result.deleted_count

