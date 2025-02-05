from typing import Annotated

from fastapi import Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from .env import Environment

env = Environment()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


async def get_current_user(req: Request, token: Annotated[str, Depends(oauth2_scheme)]):
    auth_header = req.headers.get("Authorization")
    if auth_header and auth_header.startswith("Bearer "):
        token = auth_header[7:]
        try:
            payload = jwt.decode(token, env.SECRET_KEY,
                                 algorithms=[env.ALGORITHM])
            
            email = payload.get('sub')
            if email is None:
                raise HTTPException(status_code=401, detail="Invalid Token")
            return email
        except JWTError:
            raise HTTPException(status_code=401, detail="Invalid Token")
    else:
        raise HTTPException(
            status_code=401, detail="Could not find the appropriate headers")