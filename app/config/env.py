from dotenv import load_dotenv
import os

load_dotenv()


class Environment():
    def __init__(self):
        self.MONGO_URI = os.getenv("MONGO_URI")
        self.SECRET_KEY = os.getenv("SECRET_KEY")
        self.ALGORITHM = os.getenv("ALGORITHM")
        self.ACCESS_TOKEN_EXPIRE_DAYS = int(os.getenv(
            "ACCESS_TOKEN_EXPIRE_DAYS"))
        self.TOKEN_TYPE = "bearer"
        self.TOKEN_KEY = "token"
