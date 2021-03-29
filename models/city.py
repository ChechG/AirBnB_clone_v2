#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from os import getenv
import models

class City(BaseModel):
    """ The city class, contains state ID and name """
    NEW_TYPE = getenv("HBNB_TYPE_STORAGE")
    if NEW_TYPE == "db":
        __tablename__ = "cities"
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    else:
        name = ""
