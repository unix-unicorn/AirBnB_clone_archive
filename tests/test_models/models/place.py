#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel


class Place(BaseModel):
    """
    my Place class
    """
    City_id = ""
    User_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    latitude = 0.0
    price_by_night = 0
    longitude = 0.0
    Amenity_id = ""

    def __init__(self, *args, **kwargs):
        """ my init function """
        super().__init__(*args, **kwargs)
