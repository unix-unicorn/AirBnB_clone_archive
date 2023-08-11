#!/usr/bin/python3
class Review(BaseModel):
    """
    my Review class
    """
    def __init__(self):
        """my self function"""
        self.Place.id = ""
        self.User.id = ""
        self.text = ""
