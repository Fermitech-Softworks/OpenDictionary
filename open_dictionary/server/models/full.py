import typing
from open_dictionary.server.models import read, base

__all__ = ()


class UserFull(read.UserRead):
    """
    **Full** model for :class:`.database.tables.User`.
    """

    entries: typing.List[read.EntryRead]


class EntryFull(read.EntryRead):
    """
    **Full** model for :class:`.database.tables.Entry`.
    """

    author: read.UserRead
    dictionary: read.DictionaryRead


class DictionaryFull(read.DictionaryRead):
    """
    **Full** model for :class:`.database.tables.Dictionary`.
    """

    entries: typing.Optional[typing.List[read.EntryRead]]


class ServerFull(read.ServerRead):
    """
    **Full** model for :class:`.database.tables.Dictionary`.
    """

    admin: read.UserRead


class Planetarium(base.ApiModel):
    """
    **Planetarium-compliant** model for :class:`.database.tables.Server`.
    """

    version: str
    type: str
    oauth_public: str
    server: ServerFull
