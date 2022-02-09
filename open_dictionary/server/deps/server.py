import json
from open_dictionary.database import tables, engine
from open_dictionary.server import crud
from open_dictionary.server.deps.database import dep_session
from open_dictionary.server.errors import ResourceNotFound
import fastapi

__all__ = (
    "dep_server",
)


def dep_server(session: engine.Session = fastapi.Depends(dep_session)):
    try:
        server = crud.quick_retrieve(session, tables.Server)
    except ResourceNotFound:
        server = crud.quick_create(session, tables.Server(name="Unconfigured OpenDictionary Server",
                                                          motd="As an administrator, please configure me.",
                                                          logo_uri="", custom_colors=json.dumps({})))
    return server
