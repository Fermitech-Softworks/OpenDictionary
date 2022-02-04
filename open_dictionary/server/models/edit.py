import typing as t
from uuid import UUID

from pydantic import HttpUrl

from open_dictionary.database import tables
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
    email: str
    password: str

    class Config(base.ApiORMModel.Config):
        schema_extra = {
            "example": {
                "username": "Nemesis",
                "email": "name@domain.com",
                "password": "password"
            },
        }


class EntryEdit(base.ApiORMModel):
    """
    **Edit** model for :class:`.database.tables.Entry`.
    """

    term: str
    definition: str
    examples: str
    author_id: UUID
    dictionary_id: UUID

    class Config(base.ApiORMModel.Config):
        schema_extra = {
            "example": {
                "term": "Supercazzola",
                "definition": "A complex phrase that means nothing.",
                "examples": "Tarapia Tapioco, is the Supercazzola ready or not? If so, send it to posterdati.",
                "author_id": "a0da6178-d1d3-48ef-984c-7bb8a75c6d3b",
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
                "term": "Personal Dictionary",
                "definition": "Emìglian",
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

    class Config(base.ApiORMModel.Config):
        schema_extra = {
            "example": {
                "term": "Server custom name",
                "motd": "This is a custom server.",
                "logo_uri": "https://c.tenor.com/yheo1GGu3FwAAAAd/rick-roll-rick-ashley.gif",
                "custom_colors": "{...}",
            },
        }