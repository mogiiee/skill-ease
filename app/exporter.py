import os
from dotenv import load_dotenv

load_dotenv()


realcluster = os.environ.get("CLUSTER")
db_name = os.environ.get("DB")


###COLECTIONS
complete_user = os.environ.get("USER_COLLECTION")

post_collection = os.environ.get("TOTAL_POSTS_COLLECTION")

job_collection = os.environ.get("TOTAL_JOBS_COLLECTION")
