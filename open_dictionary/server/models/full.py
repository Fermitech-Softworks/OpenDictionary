import typing
import typing as t

from open_dictionary.server.models import read

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

    entries: typing.Optional[read.EntryRead]


class ServerFull(read.ServerRead):
    """
    **Full** model for :class:`.database.tables.Dictionary`.
    """

    admin: read.UserRead
