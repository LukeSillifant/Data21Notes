import pymongo
from pprint import pprint

client = pymongo.MongoClient()
print(client)

db = client['starwars']

print(db)

# python uses snake_case instead of Camel case for commands unlike mongodb

# luke = db.chardemo.find({"name": "Luke Skywalker"})
# Wrapped up in a cursor object. They are iterables and can be converted into a list.

luke = db.chardemo.find_one({"name": "Luke Skywalker"})
blue = db.chardemo.find({"eye_color": "blue"})
droids = db.chardemo.find({"species.name": "Droid"})
vader = db.chardemo.find_one({"name": "Darth Vader"}, {"name": 1, "height": 1, "_id": 0})
yellow = db.chardemo.find({"eye_color": "yellow"}, {"name": 1, "_id": 0})
male = db.chardemo.find({"gender": "male"}, {"name": 1, "_id": 0}).limit(3)
alderaan = db.chardemo.find({"homeworld.name": "Alderaan", "species.name": "Human"}, {"name": 1, "_id": 0})

avg_female_height = db.chardemo.aggregate([
    {"$match": {"gender": "female", "height": {"$ne": float("nan")}}},
    {"$group": {"_id": "$gender", "average": {"$avg": "$height"}}}
])

tallest_char = db.chardemo.aggregate([
    {"$match": {"height": {"$ne": float("nan")}}},
    {"$group": {"_id": None, "max": {"$max": "$height"}}}
]).next()['max']

find_tallest_char = db.chardemo.find({"height": tallest_char}, {"name": 1, "height": 1, "_id": 0})

# print(luke)
#
# People with blue eyes
# blue_names = map(lambda x: x["name"], blue)
# print(list(blue_names))
#
# Name of all droid types
# for char in droids:
#     print(char['name'])
#
# Print Vader's height and name
# print(vader)
#
# Characters with yellow eyes
# for char in yellow:
#     print(char["name"])

# First 3 males
# for char in male:
#     print(char["name"])

# Humans on alderaan
# for char in alderaan:
#     print(char["name"])

# Average female height
#print(avg_female_height.next())

# Find tallest character/s
# for char in find_tallest_char:
#     print(char["name"], char["height"])