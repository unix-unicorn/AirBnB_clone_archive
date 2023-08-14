#!/usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
    """
    my new class user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """my initionalize function """
        super().__init__(*args, **kwargs)
