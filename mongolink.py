import pymongo
from pprint import pprint

# I think my IP is not static, so double check.
client = pymongo.MongoClient("mongodb://3.67.136.127:27017/demo")
print(client)

db = client['demo']

test = db.hello.find_one({})

print(test)