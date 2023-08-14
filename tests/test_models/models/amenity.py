#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    my BaseModel class
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """ my init function """
        super().__init__(*args, **kwargs)
