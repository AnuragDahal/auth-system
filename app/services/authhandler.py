from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from jose import jwt
from datetime import timedelta
from app.utils.response import send_response
from ..config.env import Environment
from .errorhandlers import ErrorHandler
from ..utils.jwtutil import create_access_token
from ..utils.passhashutils import Encrypt
from ..config.database import user_collection
from ..config.database import user_collection
from ..models import schemas

env = Environment()
SECRET_KEY = env.SECRET_KEY
ALGORITHM = env.ALGORITHM
ACCESS_TOKEN_EXPIRE_DAYS = env.ACCESS_TOKEN_EXPIRE_DAYS
TOKEN_TYPE = env.TOKEN_TYPE
TOKEN_KEY = env.TOKEN_KEY


class Validate:
    @staticmethod
    async def verify_email(email: str):
        check_email = await user_collection.find_one({"email": email})
        if check_email:
            return True
        return False


class AuthHandler:
    @staticmethod
    async def handleSignUp(request: schemas.UserCreate):
        duplicate_user = await Validate.verify_email(request.email)
        if duplicate_user:
            return ErrorHandler.ALreadyExists("User already exists")
        hashed_password = Encrypt.hash_password(request.password)
        user_data = {
            **request.model_dump(exclude={"password"}), "password": hashed_password, "isEmailVerified": False}
        await user_collection.insert_one(user_data)
        return send_response(message="User created successfully")

    @staticmethod
    async def handleLogin(request: OAuth2PasswordRequestForm = Depends()):
        user_email = await user_collection.find_one({"email": request.username})
        if user_email and Encrypt.verify_password(request.password, user_email["password"]):
            access_token_expires = timedelta(
                days=ACCESS_TOKEN_EXPIRE_DAYS)
            access_token = create_access_token(
                data={"sub": user_email["email"]}, expires_delta=access_token_expires)

            response = JSONResponse(
                content={"access_token": access_token,
                         "token_type": TOKEN_TYPE}
            )
            response.set_cookie(
                key=TOKEN_KEY,
                value=access_token,
                httponly=True,
                max_age=int(access_token_expires.total_seconds()),
                expires=int(access_token_expires.total_seconds()),
                samesite="None",
                secure=True,
                path="/"
            )
            return send_response(message="User logged in successfully", data={
                "access_token": access_token,
            })
        return ErrorHandler.NotFound("User not found")
