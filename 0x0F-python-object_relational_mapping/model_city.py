#!/usr/bin/python3
"""
contains the class definition of a City
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Class State inherits from Base"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
