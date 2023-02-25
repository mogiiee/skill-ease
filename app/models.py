from pydantic import BaseModel


class CreatorSignUp(BaseModel):
    _id: 0
    name: str
    email: str
    password: str
    creator = "yes"
    profile_photo_link : str
    discription : str
    qualifications: str
    creator_attributes_jobs =[]
    creator_attributes_courses = []
    creator_attributes_sessions = []
    tags = []


class UserSignUp(BaseModel):
    _id: 0
    first_name: str
    last_name: str
    email: str
    password: str
    creator = "no"
    user_attributes = []
    registered_courses= []


class LoginSchema(BaseModel):
    email: str
    password: str


class JobSchema(BaseModel):
    confirm_email: str
    position: str
    stipend: float
    title: str
    company: str
    description: str
    qualification: str
    experience: str
    creator= "yes"
    link:str

class CourseSchema(BaseModel):
    confirm_email: str
    title: str
    professor_name: str
    description: str
    qualification: str
    experience: str
    creator= "yes"
    video_link:str
    tags_of_course: str
    registered_students = []

class mentor(BaseModel):
    _id: 0
    name: str
    email: str
    password: str
    creator = "yes"
    profile_photo_link : str
    discription : str
    creator_attributes_jobs =[]
    creator_attributes_courses = []
    tags = []

class RegisterForJob(BaseModel):
    comfirm_email: str
    course_title: str
    course_owner_email :str
    creator =  "no"

