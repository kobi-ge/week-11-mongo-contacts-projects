from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv("MONGO_HOST")
PORT = int(os.getenv("MONGO_PORT"))
DB = os.getenv("MONGO_DB")

class MongodbInstance:
    def __init__(self):
        self.client = MongoClient(host= HOST, port=PORT)

    def get_collection(self):
        database = self.client[DB]
        collection = database['contacts']
        return collection

