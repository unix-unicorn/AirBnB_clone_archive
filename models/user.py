#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
class User(BaseModel):
    """
    my new class user
    """
    no_users = 0


    def __init__(self):
        """my initionalize function """
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        User.no_users += 1
