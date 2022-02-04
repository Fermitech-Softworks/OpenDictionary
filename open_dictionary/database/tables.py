import uuid

import sqlalchemy.orm
from sqlalchemy import Column, String, LargeBinary, ForeignKey, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

__all__ = (
    "Base",
    "User",
    "Entry",
    "Dictionary",
    "Server"
)

Base = sqlalchemy.orm.declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(LargeBinary, nullable=True)

    entries = relationship("Entry", back_populates="author")
    admin_of = relationship("Server", back_populates="admin")


class Entry(Base):
    __tablename__ = "entries"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    term = Column(String, nullable=False)
    definition = Column(String, nullable=False)
    examples = Column(String)

    author_id = Column(UUID, ForeignKey("users.id"), nullable=False)
    dictionary_id = Column(UUID, ForeignKey("dictionaries.id"), nullable=False)
    author = relationship("User", back_populates="entries")
    dictionary = relationship("Dictionary", back_populates="entries")


class Dictionary(Base):
    __tablename__ = "dictionaries"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False, unique=True)
    language = Column(String, nullable=False)

    entries = relationship("Entry", back_populates="dictionary")


class Server(Base):
    __tablename__ = "servers"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    motd = Column(String)
    logo_uri = Column(String)
    custom_colors = Column(JSON)

    admin_id = Column(UUID, ForeignKey("users.id"))
    admin = relationship("User", back_populates="admin_of")
