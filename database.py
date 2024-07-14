from pymongo import MongoClient
from bson.objectid import ObjectId
from pymongo.errors import ConnectionFailure

#Connection String MongoDB
MONGO_URI = "mongodb://localhost:27017/"
DATABASE_NAME = "school"
COLLECTION_NAME = "students"

#MONGO Connection
try:
    client = MongoClient(MONGO_URI)
    db = client[DATABASE_NAME]
    collection = db[COLLECTION_NAME]
    print("Connected to MongoDB")
except ConnectionFailure:
    print("Failed to connect to MongoDB")


#CRUD
def create_student(student_data):
    result = collection.insert_one(student_data)
    return str(result.inserted_id)

def get_student_by_id(student_id):
    student = collection.find_one({"_id": ObjectId(student_id)})
    if student:
        student["_id"] = str(student["_id"])
    return student

def update_student(student_id, student_data):
    result = collection.update_one({"_id": ObjectId(student_id)}, {"$set": student_data})
    return result.modified_count > 0

def delete_student(student_id):
    result = collection.delete_one({"_id": ObjectId(student_id)})
    return result.deleted_count > 0

def get_all_students():
    students = collection.find()
    student_list = []
    for student in students:
        student["_id"] = str(student["_id"])
        student_list.append(student)
    return student_list