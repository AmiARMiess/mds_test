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
collection = database.get_collection('film')


# Group by release_year to see unique years
# query = [ 
#     { "$group" : { "_id" : "$release_year" } } ]

# data = collection.aggregate(query)

# for doc in data:
#     print(doc)


# Group by release_year and limit to 5
# query = [ 
#     { "$group" : { "_id" : "$release_year" } },
#     { "$limit" : 5}
#     ]
# data = collection.aggregate(query)

# for doc in data:
#     print(doc)


# Project only title and release_year fields
# query = [ 
#     { "$project" : {
#         "title" : 1,
#         "release_year" : 1,
#         "_id" : 0
#     }},
#     { "$limit" : 5}
#     ]
# data = collection.aggregate(query)

# for doc in data:
#     print(doc)


# Sort by release_year descending
# query = [ 
#     { "$project" : {
#         "title" : 1,
#         "release_year" : 1,
#         "_id" : 0
#     }},
#     { "$sort" : {"release_year" : -1}},
#     { "$limit" : 5}
#     ]
# data = collection.aggregate(query)

# for doc in data:
#     print(doc)


# Match films from 2006, sort by title
# query = [ 
#     { "$match" : { "release_year" : 2006}},
#     { "$project" : {
#         "title" : 1,
#         "release_year" : 1,
#         "_id" : 0
#     }},
#     { "$sort" : {"title" : 1}},
#     { "$limit" : 5}
#     ]
# data = collection.aggregate(query)

# for doc in data:
#     print(doc)


# Group by rating and calculate average rental_rate
# query = [ 
#     { "$group": {
#         "_id": "$rating",
#         "avgRate": { "$avg": "$rental_rate" },
#         "count": { "$sum": 1 }
#     }},
#     { "$sort": { "_id": 1 }},
#     { "$limit" : 5}
# ]
# data = collection.aggregate(query)

# for doc in data:
#     print(doc)


# Count films from 2006
# query = [ 
#     { "$match" : { "release_year" : 2006}},
#     { "$count" : "totalFilms2006"}    ]
# data = collection.aggregate(query)

# for doc in data:
#     print(doc)