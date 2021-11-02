import pymongo

# connection
client = pymongo.MongoClient("mongodb+srv://<username>:<password>@<host>/<database>?retryWrites=true&w=majority", serverSelectionTimeoutMS=100000)
print("> connected")
db = client["mojidb"]
collection = db["configs"]
print("> found da database and collection")

#   serverinfo
try:
    print(client.server_info())
    print("\nconnected to the server")
except Exception as error:
    print(f"unable to connect to the server: {error}")

#   insert data
collection.insert_one(
    {
        "_id": "formats",
        "datetime": "%A %d, %B %Y %I:%M%p",
        "logging": "%(asctime)s:%(levelname)s:%(name)s: %(message)s"
    }
)
print('> inserted')

#   update data
collection.update_one(
    {"_id": "features"},
    {
        "$set": {
            "slashcommand": "moew",
            "meme": "on",
        }
    }
)
print('> updated')

#   delete
collection.delete_one({"_id": "features"})
print("> deleted")

# find
datas = collection.find_one({"_id": "formats"})
print(datas)
