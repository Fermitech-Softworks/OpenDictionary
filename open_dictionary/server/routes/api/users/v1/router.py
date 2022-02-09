from open_dictionary.server import models
import fastapi
from fastapi import Depends
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
async def read_self(current_user: tables.User = fastapi.Depends(deps.dep_user)):
    return current_user


@router.put("/self", dependencies=[Depends(auth.implicit_scheme)], response_model=models.full.UserFull)
async def edit_self(new_user: models.edit.UserEdit, current_user: tables.User = fastapi.Depends(deps.dep_user),
                    session: Session = fastapi.Depends(deps.dep_session)):
    crud.quick_update(session, current_user, new_user)
    return current_user
