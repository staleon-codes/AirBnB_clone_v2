#!/usr/bin/python3
"""Place Module for HBNB project."""

from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey(
                          'places.id'), nullable=False, primary_key=True),
                      Column('amenity_id', String(60), ForeignKey(
                          'amenities.id'), nullable=False, primary_key=True)
                      )


class Place(BaseModel, Base):
    """A place to stay."""

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    reviews = relationship('Review', cascade='delete', backref='place')
    amenities = relationship('Amenity', secondary=place_amenity,
                             viewonly=False, back_populates="place_amenities")

    # review for Filestorage
    # -----------------------------------------
    # @property
    # def reviews(self):
    #     """reviews getter"""
    #     return self.reviews
    # amenity for DBStorage
    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def reviews(self):
            from models.review import Review
            reviews_list = []
            for review in storage.all(Review).values():
                if class_obj.place_id == self.id:
                    reviews_list.append(review)
            return reviews_list

        @property
        def amenities(self):
            from models.amenity import Amenity
            amenities_list = []
            for review in storage.all(Review).values():
                if class_obj.amenity_ids == self.id:
                    amenities_list.append(review)
            return amenities_list
        # TODO amenities Setter
