from bson import ObjectId
from . import database, responses
import bcrypt


async def inserter(metadata: dict):
    database.user_collection.insert_one(metadata)
    return responses.response(True, "inserted successfully", metadata)


async def job_inserter(metadata: dict):
    await database.job_collection.insert_one(metadata)
    return responses.response(True, "inserted successfully", metadata)

async def course_inserter(metadata: dict):
    await database.course_collection.insert_one(metadata)
    return responses.response(True, "inserted successfully", metadata)

async def find_user_email(email):
    user = database.user_collection.find_one({"email": email})
    if not user:
        return responses.response(False, "does not exist", email)
    return user

def creator_attributes_jobs_updater(WrongValue,CorrectValue):
    database.user_collection.update_one({"creator_attributes_jobs":WrongValue},{"$set":{"creator_attributes_jobs":CorrectValue}}, upsert =True)

def creator_attributes_courses_updater(WrongValue,CorrectValue):
    database.user_collection.update_one({"creator_attributes_courses":WrongValue},{"$set":{"creator_attributes_courses":CorrectValue}}, upsert =True)


def deleter(id):
    database.user_collection.delete_one({"_id": ObjectId(id)})
    return responses.response(True, "deleted", None)


async def email_finder(email):
    existing_user = database.user_collection.find_one({"email": email})
    if existing_user is not None:
        return False
    else:
        return True


async def check_duplicate_email(email: str):
    existing_user = await database.user_collection.find_one({"email": email})
    return existing_user is not None


def hash_password(password: str) -> str:
    # Hash the password using bcrypt
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    # Return the hashed password as a string
    return hashed_password.decode("utf-8")


async def verify_credentials(username: str, password: str) -> bool:
    user = await find_user_email(username)
    if user is None:
        return False
    hashed_password = user["password"].encode("utf-8")
    is_valid_password = bcrypt.checkpw(password.encode("utf-8"), hashed_password)
    return is_valid_password

def creator_or_user(email) -> bool:
    full_profile=  email_finder(email)
    if full_profile["creator"] == "no":
        return False
    if full_profile["creator"] == "yes":
        return True