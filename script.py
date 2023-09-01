import pymongo
import json

# Connect to MongoDB
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['courses']
collection = db['courses']

with open('courses.json', 'r') as f:
    courses = json.load(f)


# Create index for efficient retrieval
collection.create_index('name')

# add rating field to each course
for course in courses:
    course['rating'] = {'total': 0, 'count': 0}

# add rating field to each chapter
for course in courses:
    for chapter in course['chapters']:
        chapter['rating'] = {'total': 0, 'count': 0}

# Add courses to collection
for course in courses:
    collection.insert_one(course)

# Close MongoDB connection
client.close()