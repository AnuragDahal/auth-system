from fastapi import APIRouter, Depends
from app.services.userhandler import UserManager
from app.config.dependencies import get_current_user
from ..models import schemas

router = APIRouter(prefix="/user", tags=["User"])


@router.get("/profile", response_model=schemas.UserResponseModel)
async def getUserProfile(email: str = Depends(get_current_user)):
    user_profile = await UserManager.getUserProfile(email)
    return user_profile
