#!/usr/bin/python3
from models.base_model import BaseModel
class State(BaseModel):
    """
    my state class
    """
    name = ""


    def __init__(self, *args, **kwargs):
        """my init function"""
        super().__init__(*args, **kwargs)
