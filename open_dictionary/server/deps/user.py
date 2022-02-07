from uuid import UUID

import fastapi
from fastapi import Security
from fastapi_auth0 import Auth0User
from open_dictionary.database import tables, engine
from open_dictionary.server import crud
from open_dictionary.server.deps.database import dep_session
from open_dictionary.server.errors import InvalidCredentials
from open_dictionary.server.authentication import auth

__all__ = (
    "dep_user",
)


def dep_user(
        session: engine.Session = fastapi.Depends(dep_session),
        user: Auth0User = Security(auth.get_user)
):
    try:
        email: str = user.email
        if email is None:
            raise InvalidCredentials
    except Exception:
        raise InvalidCredentials
    user_db = crud.quick_retrieve(session, tables.User, email=user.email)
    if not user_db:
        crud.quick_create(session, tables.User(username=user.email, email=user.email))
    return user_db
