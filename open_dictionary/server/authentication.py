from datetime import datetime, timedelta
from typing import Optional
from os import environ

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel

from open_dictionary.database import tables
from open_dictionary.server.crud import quick_retrieve
from open_dictionary.database.engine import Session

SECRET_KEY = environ["JWT_KEY"]
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 120


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/user/v1/login")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def check_password(h, password):
    return pwd_context.verify(password, h)


def get_hash(password):
    return pwd_context.hash(password)


def authenticate_user(email: str, password: str):
    with Session() as db:
        user: tables.User = quick_retrieve(db, tables.User, email=email)
        if not user:
            return False
        if not check_password(user.password, password):
            return False
        return user


def create_token(data: dict):
    encode = data.copy()
    encode.update({"exp": datetime.utcnow() + timedelta(ACCESS_TOKEN_EXPIRE_MINUTES)})
    return jwt.encode(encode, SECRET_KEY, ALGORITHM)



