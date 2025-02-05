# from pymongo import MongoClient, IndexModel, ASCENDING
from motor.motor_asyncio import AsyncIOMotorClient
from .env import Environment

env = Environment()


client = AsyncIOMotorClient(env.MONGO_URI)

db = client["auth-system"]

user_collection = db["users"]