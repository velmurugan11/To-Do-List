from pymongo import MongoClient

def get_database():
    client=MongoClient("mongodb://localhost:27017/")
    return client["todo_app"]