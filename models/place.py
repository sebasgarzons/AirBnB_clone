#!/usr/bin/python3
"""
Creating of class Place that inherit from BaseModel
"""


class Place(BaseModel):
    """Class Place with the following public class attributes"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_nigth = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []