import typing as t
from uuid import UUID
from open_dictionary.server.models import base

__all__ = (
    "UserEdit",
    "EntryEdit",
    "DictionaryEdit",
    "ServerEdit"
)


class UserEdit(base.ApiORMModel):
    """
    **Edit** model for :class:`.database.tables.User`.
    """

    username: str

    class Config(base.ApiORMModel.Config):
        schema_extra = {
            "example": {
                "username": "Nemesis",
            },
        }


class EntryEdit(base.ApiORMModel):
    """
    **Edit** model for :class:`.database.tables.Entry`.
    """

    term: str
    definition: str
    examples: str
    dictionary_id: UUID

    class Config(base.ApiORMModel.Config):
        schema_extra = {
            "example": {
                "term": "Supercazzola",
                "definition": "A complex phrase that means nothing.",
                "examples": "Tarapia Tapioco, is the Supercazzola ready or not? If so, send it to posterdati.",
                "dictionary_id": "b0rc6178-d1d3-48ef-984c-7bb8a75c6d3b"
            },
        }


class DictionaryEdit(base.ApiORMModel):
    """
    **Edit** model for :class:`.database.tables.Dictionary`.
    """

    name: str
    language: str

    class Config(base.ApiORMModel.Config):
        schema_extra = {
            "example": {
                "name": "Personal Dictionary",
                "language": "Emìglian",
            },
        }


class ServerEdit(base.ApiORMModel):
    """
    **Edit** model for :class:`.database.tables.Server`.
    """

    name: str
    motd: str
    logo_uri: t.Optional[str]
    custom_colors: t.Optional[str]