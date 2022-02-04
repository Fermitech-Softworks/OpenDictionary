from uuid import UUID

import fastapi

from open_dictionary.database import tables, engine
from open_dictionary.server import crud
from open_dictionary.server.deps.database import dep_session

__all__ = (
    "dep_user",
)


def dep_user(
        session: engine.Session = fastapi.Depends(dep_session),
        user: str = fastapi.Path(...)
):
    try:
        uuid = UUID(user)
    except ValueError:
        return crud.quick_retrieve(session, tables.User, crystal=user)
    else:
        return crud.quick_retrieve(session, tables.User, id=uuid)
