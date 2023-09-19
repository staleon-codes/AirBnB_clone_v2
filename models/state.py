#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
from models import storage


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='delete', backref='state')
    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            from models.city import City
            cities_list = []
            for city in storage.all(City).values():
                if class_obj.state_id == self.id:
                    cities_list.append(city)
            return cities_list
