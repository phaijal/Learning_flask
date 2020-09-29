from flask import Flask
from flask import request
import pymongo
from pymongo import MongoClient
import json
from bson import json_util

app = Flask(__name__)
cluster = MongoClient("mongodb+srv://akash:akash@cluster0.zqitl.mongodb.net/<dbname>?retryWrites=true&w=majority")

db = cluster["dbname"]
collection = db["coll"]

#collection.insert_one({"_id": 1, "name": "sadff asfdasf"})




@app.route("/")
def getval():
    all_names = list(collection.find({}))
    out = f"names: "
    for n in all_names:
        s = n["name"]
        out += f"{s} "
    return out


@app.route("/add/<name>")
def addname(name):
    collection.insert_one({"name": name})
    return f"added {name}"


@app.route("/addval", methods=["POST"])
def addval():
    request_payload = request.json
    print(request_payload)
    print("hjh")
  #  inf = request_payload['info']
  #  collection.insert_one({"name": "ttt"})
    return f"added"

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")