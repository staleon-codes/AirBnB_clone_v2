#!/usr/bin/python3
"""Audit module for the HBNB project."""

from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey


class Review(BaseModel, Base):
    """Audit class to store review information."""

    __tablename__='reviews'
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    text = Column(String(1024), nullable=False)
