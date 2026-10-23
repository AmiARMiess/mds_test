from pymongo import MongoClient
from urllib.parse import quote_plus

# Direct MongoDB connection
host = 'localhost'
port = 27017

# Format the connection string
uri = f"mongodb://{host}:{port}"

client = MongoClient(uri)

# Test connection
client.admin.command('ping')
print("✓ Successfully connected to MongoDB")
print(f"Connected to: {host}")

# Use the sakila database
database = client['sakila']
print(f"Using database: {database.name}")

# sakila has 'film' collection (similar to video_movies)
# collection = database.get_collection('film')


# Query films from 2006 with PG rating
# for doc in collection.find({"release_year" : 2006, "rating": "PG"}).limit(3):
#     print(doc)

# Find films with length less than 50 minutes
# for doc in collection.find({"length":{"$lt":50}}).limit(5):
#     print(doc)

# Find films with length less than or equal to 50 minutes
# for doc in collection.find({"length":{"$lte":50}}).limit(5):
#     print(doc)

# Find films with length greater than 180 minutes
# for doc in collection.find({"length":{"$gt":180}}).limit(5):
#     print(doc)

# Find films with length greater than or equal to 180 minutes
# for doc in collection.find({"length":{"$gte":180}}).limit(5):
#     print(doc)

# Find films with rating not equal to PG
# for doc in collection.find({"rating":{"$ne":"PG"}}).limit(5):
#     print(doc)

# Find films with specific ratings
# for doc in collection.find({"rating":{"$in":["G", "PG", "NC-17"]}}).limit(10):
#     print(doc)

# Find films that are either rated NC-17 OR have title "ACADEMY DINOSAUR"
# for doc in collection.find({"$or":[{"rating":"NC-17"},{"title": "ACADEMY DINOSAUR"}]}).limit(10):
#     print(doc)

# Same query with sort by length and limit
# for doc in collection.find({"$or":[{"rating":"NC-17"},{"title": "ACADEMY DINOSAUR"}]}).sort("length").limit(5):
#     print(doc)