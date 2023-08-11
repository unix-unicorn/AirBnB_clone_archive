#!/usr/bin/python3
class user(BaseModel):
    """
    my new class user
    """
    no_users = 0


    def __init__(self, email, password, first_name, last_name):
        """my initionalize function """
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        user.no_users += 1
