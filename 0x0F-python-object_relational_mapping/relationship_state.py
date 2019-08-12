#!/usr/bin/python3
""" docdddd """

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    """ docdddd """
    __tablename__ = "states"
    id = Column('id', Integer, primary_key=True,
                autoincrement=True, unique=True, nullable=False)
    name = Column('name', String(128), nullable=False)
    cities = relationship('City', backref="state")
