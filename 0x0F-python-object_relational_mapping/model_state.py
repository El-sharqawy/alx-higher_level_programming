#!/usr/bin/python3

"""Class definition of State"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

metaData = MetaData()
Base = declarative_base()


class State(Base):
    """Class with id and name for states"""

    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
