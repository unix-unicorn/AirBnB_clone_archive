#!/usr/bin/python3
class Amenity(BaseModel):
    """
    my BaseModel class
    """
    name = ""
    def __init__(self,*args, **kwargs):
        """ my init function """
        super().__init__(*args, **kwargs)
