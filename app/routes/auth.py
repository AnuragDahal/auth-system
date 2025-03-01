from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, status
from ..services.authhandler import AuthHandler
from ..models import schemas
from ..services.errorhandlers import ErrorHandler
import re

router = APIRouter(prefix="/auth", tags=["Auth"])

PASSWORD_REGEX = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@$!%*?&])[A-Za-z\\d@$!%*?&]{8,16}$"


@router.post("/signup", status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponseModel)
async def userSignup(request: schemas.UserCreate):
    password = request.password
    if len(password) < 8 or len(password) > 16:
        return ErrorHandler.Error("Password must be between 8 to 16 characters long")
    if not any(char.isupper() for char in password):
        return ErrorHandler.Error("Password must contain at least one uppercase letter")
    if not any(char in "@$!%*?&" for char in password):
        return ErrorHandler.Error("Password must contain at least one special character (@$!%*?&)")
    if not any(char.isdigit() for char in password):
        return ErrorHandler.Error("Password must contain at least one numeric character")
    if not re.match(PASSWORD_REGEX, password):
        return ErrorHandler.Error("Password validation failed")
    new_user = await AuthHandler.handleSignUp(request)
    return new_user


@router.post("/login", status_code=status.HTTP_200_OK, response_model=schemas.UserResponseModel)
async def userLogin(request: OAuth2PasswordRequestForm = Depends()):
    user = await AuthHandler.handleLogin(request)
    return user
