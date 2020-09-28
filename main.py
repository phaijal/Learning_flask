from flask import Flask
import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://akash:akash@cluster0.zqitl.mongodb.net/<dbname>?retryWrites=true&w=majority")

db = cluster["dbname"]
collection = db["coll"]

#collection.insert_one({"_id": 1, "name": "sadff asfdasf"})

app = Flask(__name__)


@app.route("/")
def getval():
    all_names = list(collection.find({}))
    out = f"names: "
    for n in all_names:
        s = n["name"]
        out += f"{s} "
    return out

if __name__ == "__main__":
    app.run()