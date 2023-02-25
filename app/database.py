from . import exporter
import pymongo


cluster = pymongo.MongoClient(exporter.realcluster)

db = cluster[exporter.db_name]

user_collection = db[exporter.complete_user]

course_collection = db[exporter.post_collection]

job_collection = db[exporter.job_collection]
