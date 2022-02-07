import os

from open_dictionary.server import models
import bcrypt
import fastapi
from fastapi import FastAPI, Depends, Security
from fastapi_auth0 import Auth0, Auth0User
from open_dictionary.server import crud
from open_dictionary.server import deps
from open_dictionary.database.engine import Session
from open_dictionary.database import tables
from open_dictionary.server.authentication import auth

router = fastapi.routing.APIRouter(
    prefix="/api/user/v1",
    tags=["User v1"]
)


@router.get("/self", dependencies=[Depends(auth.implicit_scheme)], response_model=models.full.UserFull)
def get_secure(current_user: tables.User = fastapi.Depends(deps.dep_user)):
    return current_user
