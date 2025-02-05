from fastapi.responses import JSONResponse
from typing import Optional


def send_response(message: str, data: Optional[dict]):
    response_content = {
        "status": "success",
        "message": message,
        "data": data
    }
    return JSONResponse(content=response_content)
