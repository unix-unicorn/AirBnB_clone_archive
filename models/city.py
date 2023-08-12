#!/usr/bin/python3
class City(BaseModel):
    """
    my class City
    """
    State.id = ""
    name = ""

    def __init__(self,*args, **kwargs):
        """ my init function """
        super().__init__(*args, **kwargs)
