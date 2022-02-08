from uuid import UUID
from open_dictionary.database import tables, engine
from open_dictionary.server import crud
from open_dictionary.server.deps.database import dep_session
import fastapi

__all__ = (
    "dep_dictionaries",
    "dep_dictionary",
)


def dep_dictionaries(session: engine.Session = fastapi.Depends(dep_session)):
    return session.query(tables.Dictionary).all()


def dep_dictionary(dictionary_id: UUID, session: engine.Session = fastapi.Depends(dep_session)):
    return crud.quick_retrieve(session, tables.Dictionary, id=dictionary_id)
