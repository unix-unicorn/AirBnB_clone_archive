#!/usr/bin/python3
from models.base_model import BaseModel


class Review(BaseModel):
    """
    my Review class
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """my self function"""
        super().__init__(*args, **kwargs)
