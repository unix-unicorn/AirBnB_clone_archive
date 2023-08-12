#!/usr/bin/python3
class Review(BaseModel):
    """
    my Review class
    """
    Place.id = ""
    User.id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """my self function"""
        super().__init__(*args, **kwargs)
