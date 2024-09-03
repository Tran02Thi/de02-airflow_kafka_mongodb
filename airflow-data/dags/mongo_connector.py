from pymongo import MongoClient
import logging

class MongoDBConnector:
    def __init__(self, mongodb_uri, database_name, collection_name):
        self.client = MongoClient(mongodb_uri)
        self.db = self.client[database_name]
        self.collection_name = collection_name

    def create_collection(self):
        # Check if the collection already exists
        if self.collection_name not in self.db.list_collection_names():
            self.db.create_collection(self.collection_name)
            logging.info(f"Created collection: {self.collection_name}")
        else:
            logging.warning(f"Collection {self.collection_name} already exists")

    def insert_data(self, document):
        self.db[self.collection_name].insert_one(document)

    def close(self):
        self.client.close()
