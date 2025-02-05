from app.utils.response import send_response
from app.config.database import user_collection
from app.services.errorhandlers import ErrorHandler


class UserManager:
    @staticmethod
    async def getUserProfile(email: str):
        user_data = await user_collection.find_one({"email": email})
        if not user_data:
            raise ErrorHandler.ErrorNotFound("User not found")
        return send_response(message="User profile fetched successfully", data={
            "name": user_data["name"],
            "email": user_data["email"],
            "isEmailVerified": user_data["isEmailVerified"]
        })
