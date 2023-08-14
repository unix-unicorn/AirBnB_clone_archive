#!/usr/bin/python3
from models.base_model import BaseModel


class Review(BaseModel):
    """
    my Review class
    """
    Place_id = ""
    User_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """my self function"""
        super().__init__(*args, **kwargs)
