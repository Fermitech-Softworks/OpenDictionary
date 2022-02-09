from open_dictionary.server import models
import fastapi
from fastapi import Depends
from open_dictionary.server import crud
from open_dictionary.server import deps
from open_dictionary.database import tables
from open_dictionary.database.engine import Session
from fastapi_pagination import Page, paginate
from open_dictionary.server.authentication import auth
from open_dictionary.server.responses.raw import NO_CONTENT
from sqlalchemy import desc
from typing import List

router = fastapi.routing.APIRouter(
    prefix="/api/dictionary/v1",
    tags=["Dictionary v1"]
)


@router.get("/{dictionary_id}", response_model=models.full.DictionaryFull)
async def get_dictionary(dictionary: tables.Dictionary = fastapi.Depends(deps.dep_dictionary)):
    return dictionary


@router.get("/", response_model=List[models.read.DictionaryRead])
async def get_dictionaries(dictionaries: List[models.read.DictionaryRead] = fastapi.Depends(deps.dep_dictionaries)):
    return dictionaries


@router.get("/{dictionary_id}/index", response_model=Page[models.read.EntryRead])
async def get_index(session: Session = fastapi.Depends(deps.dep_session),
                    dictionary: tables.Dictionary = fastapi.Depends(deps.dep_dictionary)):
    return paginate(
        session.query(tables.Entry).filter_by(dictionary_id=dictionary.id).order_by(desc(tables.Entry.term)).all())


@router.post("/", dependencies=[Depends(auth.implicit_scheme)], response_model=models.read.DictionaryRead)
async def add_dictionary(new_dict: models.edit.DictionaryEdit,
                         current_user: tables.User = fastapi.Depends(deps.dep_admin),
                         session: Session = fastapi.Depends(deps.dep_session)):
    return crud.quick_create(session, tables.Dictionary(name=new_dict.name, language=new_dict.language))


@router.put("/{dictionary_id}", dependencies=[Depends(auth.implicit_scheme)],
            response_model=models.read.DictionaryRead)
async def update_dictionary(updated_dict: models.edit.DictionaryEdit,
                            current_user: tables.User = fastapi.Depends(deps.dep_admin),
                            session: Session = fastapi.Depends(deps.dep_session),
                            dictionary: tables.Dictionary = fastapi.Depends(deps.dep_dictionary)):
    return crud.quick_update(session, dictionary, updated_dict)


@router.delete("/{dictionary_id}", dependencies=[Depends(auth.implicit_scheme)], status_code=204)
async def delete_entry(session: Session = fastapi.Depends(deps.dep_session),
                       current_user: tables.User = fastapi.Depends(deps.dep_admin),
                       dictionary: tables.Dictionary = fastapi.Depends(deps.dep_dictionary)):
    session.delete(dictionary)
    session.commit()
    return NO_CONTENT
