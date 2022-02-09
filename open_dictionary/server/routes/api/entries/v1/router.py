from open_dictionary.server import models
import fastapi
from fastapi import Depends
from open_dictionary.server import crud
from open_dictionary.server import deps
from open_dictionary.database import tables
from open_dictionary.database.engine import Session
from fastapi_pagination import Page, paginate
from open_dictionary.server.authentication import auth
from open_dictionary.server.utilities import search
from open_dictionary.server.responses.raw import NO_CONTENT

router = fastapi.routing.APIRouter(
    prefix="/api/entry/v1",
    tags=["Entry v1"]
)


@router.post("/search", response_model=Page[models.read.EntryRead])
async def search_entries(query: str, entries=fastapi.Depends(deps.dep_entries)):
    return paginate(search(entries, query))


@router.post("/", dependencies=[Depends(auth.implicit_scheme)], response_model=models.read.EntryRead)
async def add_entry(new_entry: models.edit.EntryEdit, current_user: tables.User = fastapi.Depends(deps.dep_user),
                    session: Session = fastapi.Depends(deps.dep_session)):
    entry = tables.Entry(term=new_entry.term, definition=new_entry.definition, examples=new_entry.examples,
                         dictionary_id=new_entry.dictionary_id, author_id=current_user.id)
    session.add(entry)
    session.commit()
    return entry


@router.get("/{entry_id}", response_model=models.full.EntryFull)
async def get_entry(entry: tables.Entry = fastapi.Depends(deps.dep_entry)):
    return entry


@router.put("/{entry_id}", dependencies=[Depends(auth.implicit_scheme)], response_model=models.full.EntryFull)
async def update_entry(update: models.edit.EntryEdit, entry: tables.Entry = fastapi.Depends(deps.check_owner),
                       current_user: tables.User = fastapi.Depends(deps.dep_user),
                       session: Session = fastapi.Depends(deps.dep_session)):
    return crud.quick_update(session, entry, update)


@router.delete("/{entry_id}", dependencies=[Depends(auth.implicit_scheme)], status_code=204)
async def delete_entry(session: Session = fastapi.Depends(deps.dep_session),
                       entry: tables.Entry = fastapi.Depends(deps.check_owner)):
    session.delete(entry)
    session.commit()
    return NO_CONTENT
