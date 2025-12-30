from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import os
from dotenv import load_dotenv

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
            self.db = client.contacts_db
            self.collection = self.db.contacts
            return "Successfully connected to MongoDB"
        
        except ConnectionFailure as e:
            return f"failed to connect to db: {e}"


    def select(self, id = None):
        if self.db is None:
            self.get_database()
        return list(self.collection.find())

    def insert(self, contact):
        contact = contact.to_dict()
        result = self.db.contacts.insert_one(contact)
        return result.inserted_id

    def update(collection, identifier):
        pass

    def delete(collection, identifier):
        pass


a = MongodbInstance()
a.get_database()
print(a.collection)
print(a.select())