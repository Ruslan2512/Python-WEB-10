from pymongo import MongoClient


def get_mongodb():
    client = MongoClient("mongodb+srv://ruslan:qwerty123@cluster.9diyzhg.mongodb.net/?retryWrites=true&w=majority")

    db = client.HM10
    return db
