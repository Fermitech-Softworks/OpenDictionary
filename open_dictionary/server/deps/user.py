from uuid import UUID

import fastapi
from jose import jwt, JWTError

from open_dictionary.database import tables, engine
from open_dictionary.server import crud
from open_dictionary.server.deps.database import dep_session
from open_dictionary.server.authentication import oauth2_scheme, SECRET_KEY, ALGORITHM, TokenData
from open_dictionary.server.errors import InvalidCredentials
from open_dictionary.server.crud import quick_retrieve

__all__ = (
    "dep_user",
)


def dep_user(
        session: engine.Session = fastapi.Depends(dep_session),
        token: str = fastapi.Depends(oauth2_scheme)
):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise InvalidCredentials
    except JWTError:
        raise InvalidCredentials
    user = quick_retrieve(session, tables.User, email=email)
    if user is None:
        raise InvalidCredentials
    return user
