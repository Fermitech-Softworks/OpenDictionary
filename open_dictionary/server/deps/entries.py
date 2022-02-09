from uuid import UUID
from open_dictionary.database import tables, engine
from open_dictionary.server import crud
from open_dictionary.server.deps.database import dep_session
from open_dictionary.server.deps.user import dep_user
from open_dictionary.server.errors import InvalidCredentials
import fastapi

__all__ = (
    "dep_entries",
    "dep_entry",
    "check_owner"
)


def dep_entries(session: engine.Session = fastapi.Depends(dep_session)):
    return session.query(tables.Entry).all()


def dep_entry(entry_id: UUID, session: engine.Session = fastapi.Depends(dep_session)):
    return crud.quick_retrieve(session, tables.Entry, id=entry_id)


def check_owner(current_user=fastapi.Depends(dep_user), entry=fastapi.Depends(dep_entry)):
    if not entry.author == current_user:
        raise InvalidCredentials
    return entry
