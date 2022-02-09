from uuid import UUID
from open_dictionary.server.models import edit
from open_dictionary.server.models import base

__all__ = (
    "UserRead",
    "EntryRead",
    "DictionaryRead",
    "ServerRead"
)


class UserRead(base.ApiORMModel):
    """
    **Read** model for :class:`.database.tables.User`.
    """

    id: UUID
    username: str
    email: str

    class Config(edit.UserEdit.Config):
        schema_extra = {
            "example": {
                **edit.UserEdit.Config.schema_extra["example"],
                "id": "70fd1bf3-69dd-4cde-9d41-42368221849f",
            },
        }


class EntryRead(edit.EntryEdit):
    """
    **Read** model for :class:`.database.tables.Entry`.
    """

    id: UUID
    author_id: UUID

    class Config(edit.EntryEdit.Config):
        schema_extra = {
            "example": {
                **edit.EntryEdit.Config.schema_extra["example"],
                "id": "70fd1bf3-69dd-4cde-9d41-42368221849f",
                "author_id": "a0da6178-d1d3-48ef-984c-7bb8a75c6d3b",
            },
        }


class DictionaryRead(edit.DictionaryEdit):
    """
    **Read** model for :class:`.database.tables.Dictionary`.
    """

    id: UUID

    class Config(edit.DictionaryEdit.Config):
        schema_extra = {
            "example": {
                **edit.DictionaryEdit.Config.schema_extra["example"],
                "id": "70fd1bf3-69dd-4cde-9d41-42368221849f",
            },
        }


class ServerRead(edit.ServerEdit):
    """
    **Read** model for :class:`.database.tables.Server`.
    """

    id: UUID