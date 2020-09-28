from flask import Flask
import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://akash:akash@cluster0.zqitl.mongodb.net/<dbname>?retryWrites=true&w=majority")

db = cluster["dbname"]
collection = db["coll"]

collection.insert_one({"_id": 0, "name": "akash singh"})
