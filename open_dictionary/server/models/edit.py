import typing as t
from uuid import UUID

from pydantic import HttpUrl

from open_dictionary.database import tables
from open_dictionary.server.models import base

__all__ = (
    "UserEdit",
)


class UserEdit(base.ApiORMModel):
    """
    **Edit** model for :class:`.database.tables.User`.
    """

    crystal: str

    class Config(base.ApiORMModel.Config):
        schema_extra = {
            "example": {
                "crystal": "77703771181817856",
            },
        }
