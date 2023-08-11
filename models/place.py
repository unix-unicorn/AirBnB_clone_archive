#!/usr/bin/python3
class Place(BaseModel):
    """
    my Place class
    """
    def __init__(self, City.id, User.id, name, description, number_rooms, number_bathrooms, max_guest, latitude, price_by_night, longitude, Amenity.id):
        """my self function"""
        self.City.id = ""
        self.User.id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.latitude = 0.0
        self.price_by_night = 0
        self.longitude = 0.0
        self.Amenity.id = []
