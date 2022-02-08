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
    prefix="/api/server/v1",
    tags=["Server v1"]
)


@router.get("/", response_model=models.full.ServerFull)
async def read_self(server=fastapi.Depends(deps.dep_server)):
    return server


@router.put("/", dependencies=[Depends(auth.implicit_scheme)], response_model=models.full.ServerFull)
async def edit_self(new_server: models.edit.ServerEdit, current_user: tables.User = fastapi.Depends(deps.dep_admin),
                    session: Session = fastapi.Depends(deps.dep_session), server=fastapi.Depends(deps.dep_server)):
    crud.quick_update(session, server, new_server)
    return server
