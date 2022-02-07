import fastapi.routing
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from open_dictionary.database import tables
from open_dictionary.server import crud
from open_dictionary.server import deps
from open_dictionary.server import models
from open_dictionary.server import responses
from open_dictionary.server import errors
from open_dictionary.server.authentication import Token, authenticate_user, create_token
import bcrypt

router = fastapi.routing.APIRouter(
    prefix="/api/user/v1",
    tags=["User v1"]
)


@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = fastapi.Depends()):
    user: tables.User = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise errors.InvalidCredentials()
    return {"access_token": create_token(data={"sub": user.email}), "token_type": "bearer"}


@router.get("/me", response_model=models.full.UserFull)
async def read_user_me(current_user: tables.User = fastapi.Depends(deps.dep_user)):
    return current_user


@router.post("/add", response_model=models.read.UserRead)
async def add_user(data: models.edit.UserEdit, session: Session = fastapi.Depends(deps.dep_session)):
    return crud.quick_create(session, tables.User(username=data.username, email=data.email,
                                                  password=bcrypt.hashpw(bytes(data.password, encoding="utf-8"),
                                                                         bcrypt.gensalt())))
