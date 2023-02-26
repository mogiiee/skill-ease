import copy
from fastapi import FastAPI, HTTPException, Request
from fastapi.encoders import jsonable_encoder
from . import models, responses, ops, database


from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def greet():
    return {"hello": "world"}


@app.post("/signup/creator", tags=["creator"])
async def creator_signup(signup_details: Request):
    infoDict = await signup_details.json()
    print(infoDict)
    infoDict = dict(infoDict)
    print(infoDict)
    # Checking if email already exists
    email_count = database.user_collection.count_documents(
        {"email": infoDict["email"]}
    )
    if email_count > 0:
        return responses.response(False, "duplicated user, email already in use", None)
    # Insert new user
    encoded_password = ops.hash_password(str(infoDict["password"]))
    infoDict['password'] = encoded_password
    json_signup_details = jsonable_encoder(infoDict)
    await ops.inserter(json_signup_details)
    return responses.response(True, "inserted", {
        infoDict
    })



@app.post("/login", tags=["login"])
async def login(login_deets:Request):
    infoDict = await login_deets.json()
    print(infoDict)
    email = infoDict['email']
    password = infoDict['password']
    # Verify credentials
    if await ops.verify_credentials(email, password):
        return responses.response(True, "logged in", {"email": email})
    else:
        raise HTTPException(401, "unauthorised login or email is wrong")


@app.post("/creator/add_job", tags=["creator"])
async def add_job(job_deets: Request):
    infoDict = await job_deets.json()
    json_job_deets = dict(infoDict)
    email = infoDict['email']
    full_profile = await ops.find_user_email(email)
    creator_user_attributes = full_profile["creator_attributes_jobs"]
    original_attributes = copy.deepcopy(full_profile["creator_attributes_jobs"])
    creator_user_attributes.append(json_job_deets)
    print(creator_user_attributes)
    ops.creator_attributes_jobs_updater(infoDict["email"],creator_user_attributes)
    ops.job_inserter(json_job_deets)
    return responses.response(True, "job posted!", infoDict)



@app.post("/creator/add_course", tags=["creator"])
async def add_course(course_deets: Request):
    infoDict = await course_deets.json()
    json_course_deets = dict(infoDict)
    email = infoDict["email"]
    full_profile = await ops.find_user_email(email)
    creator_attributes_courses = full_profile["creator_attributes_courses"]
    original_attributes = copy.deepcopy(full_profile["creator_attributes_courses"])
    creator_attributes_courses.append(json_course_deets)
    ops.creator_attributes_courses_updater(infoDict["email"],creator_attributes_courses)
    ops.course_inserter(json_course_deets)
    return responses.response(True, "course created!", infoDict)


@app.patch("/creator/session", tags=['creator'])
async def add_session(session_deets: Request):
    info_dict = await session_deets.json()
    # print(info_dict)
    info_dict = dict(info_dict)
    email = info_dict["email"]
    time = info_dict['time']
    date = info_dict['date']

    full_profile = await ops.find_user_email(email)
    creator_attributes_sessions = full_profile["creator_attributes_sessions"]
    original_creator_attributes_sessions = copy.deepcopy(full_profile["creator_attributes_sessions"])
    new_dict = {
        "time" : time,
        "date": date
     }
    
    print(new_dict)
    creator_attributes_sessions.append(new_dict)  
    print(creator_attributes_sessions)
    ops.creator_attributes_session_updater(info_dict["email"], creator_attributes_sessions)
    return responses.response(True, "session added!", creator_attributes_sessions)

    



@app.patch("/update/mentor", tags=["creator"])
async def detail_updater(new_deets: Request):
    infoDict = await new_deets.json()
    dict(infoDict)
    email = infoDict['email']
    full_profile = await ops.find_user_email(email)
    old_name = copy.deepcopy(full_profile['name'])
    old_profile_photo_link =copy.deepcopy(full_profile["profile_photo_link"])
    old_description = copy.deepcopy(full_profile["discription"])
    old_qualifications = copy.deepcopy(full_profile["qualifications"])
    new_name = infoDict["name"]
    new_profile_photo_link = infoDict['profile_photo_link']
    new_description = infoDict['description']
    new_qualification = infoDict['qualification']
    database.user_collection.update_one({"name":old_name},{"$set":{"name":new_name}})

    database.user_collection.update_one({"discription":old_description},{"$set":{"discription": new_description}})

    database.user_collection.update_one({"profile_photo_link":old_profile_photo_link},{"$set":{"profile_photo_link":new_profile_photo_link}})

    database.user_collection.update_one({"qualifications":old_qualifications},{"$set":{"qualifications":new_qualification}})

    return responses.response(True, "changed", {
        old_qualifications:new_qualification,
        old_description:new_description,
        old_name: new_name,
        old_profile_photo_link: new_profile_photo_link
    })


@app.post("/signup/user", tags=["user"])
async def user_signup(signup_details: Request):
    # Checking if email already exists
    infoDict = await signup_details.json()
    print(infoDict)
    infoDict = dict(infoDict)
    print(infoDict)
    # Checking if email already exists
    email_count = database.user_collection.count_documents(
        {"email": infoDict["email"]}
    )
    if email_count > 0:
        return responses.response(False, "duplicated user, email already in use", None)
    # Insert new user
    encoded_password = ops.hash_password(str(infoDict["password"]))
    infoDict['password'] = encoded_password
    json_signup_details = jsonable_encoder(infoDict)
    await ops.inserter(json_signup_details)
    return responses.response(True, "inserted", infoDict)







# @app.post("/user/register-course", tags=["user"])
# async def add_job(registeration_deets: models.RegisterForJob):
#     json_registeration_deets = jsonable_encoder(registeration_deets)
#     user_email = registeration_deets.comfirm_email
#     user_full_profile = await ops.find_user_email(user_email)
#     creator_email = registeration_deets.course_owner_email
#     if ops.creator_or_user(creator_email):
#         user_attributes = user_full_profile["user_attributes"]
#         original_attributes = copy.deepcopy(user_attributes)
#         user_attributes.append(json_registeration_deets)
#         ops.user_attributes_updater(original_attributes,user_attributes)


#         full_creator_profile = await ops.find_user_email(creator_email)
#         registered_users = full_creator_profile["registered_users"]
#         original_attributes = copy.deepcopy(full_creator_profile["registered_users"])
#         registered_users.append(user_full_profile)
#         ops.creator_attributes_updater(original_attributes,registered_users)
#         return responses.response(True, "course added!", str(full_creator_profile) and json_registeration_deets)


#     else: 
#         return responses.response(False, "creator email is wrong", str(creator_email) )










@app.delete("/collection/", tags=["do not touch"])
async def delete_collection():
    # Delete all documents in the user_collection
    database.user_collection.delete_one({})

    return {"success": True}

@app.get('/get_user')
async def find_user_email(email):
    user = database.user_collection.find_one({"email": email})
    print(user)
    if not user:
        return responses.response(False, "does not exist", email)
    return str(user)

