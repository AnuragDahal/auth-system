from typing import Annotated

from fastapi import Depends, HTTPException, Request, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt, ExpiredSignatureError

from .env import Environment

env = Environment()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials")
    try:
        payload = jwt.decode(token, env.SECRET_KEY, algorithms=[env.ALGORITHM])
        email = payload.get('sub')
        if email is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Token")
        return email
    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired")
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Token")
