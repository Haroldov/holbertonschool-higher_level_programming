#!/usr/bin/python3
""" docdddd """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from relationship_state import Base

class City(Base):
    """ docdddd """
    __tablename__ = "cities"
    id = Column('id', Integer, primary_key=True,
                autoincrement=True, unique=True, nullable=False)
    name = Column('name', String(128), nullable=False)
    state_id = Column('state_id', Integer,
                      ForeignKey("states.id"), nullable=False)
