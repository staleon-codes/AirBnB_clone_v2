#!/usr/bin/python3
"""The unit defines a class User."""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines an operator by various attributes."""

    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship('Place', cascade='delete', backref='user')
    reviews = relationship('Review', cascade='delete', backref='user')
