from pymongo import MongoClient


# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["school"]
collection = db["students"]

# Insert Data
students = [
    {"name": "David", "age": 24, "major": "Engineering"},
    {"name": "Emma", "age": 20, "major": "Biology"},
]
collection.insert_many(students)

# Query Data
for student in collection.find():
    print(student)