import os
import pymongo
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGODB_URI")
client = pymongo.MongoClient(MONGO_URI)
db = client["telegram_bot"]
users_collection = db["users"]
chats_collection = db["chats"]
files_collection = db["files"]
