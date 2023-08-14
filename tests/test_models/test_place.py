#!/usr/bin/python3
"""Unittest for basemodel
"""
import unittest
from models.place import Place
from models.base_model import BaseModel
from models import storage
from datetime import datetime


class TestAmna(unittest.TestCase):
    """
    test class for the max_integer() function.
    """

    place = Place()
    place.name = "Luxury Apartment"
    place.id = "456-456-456"
    place.city_id = "city-123"
    place.user_id = "user-456"
    place.description = "A luxurious apartment"
    place.number_rooms = 3
    place.number_bathrooms = 2
    place.max_guest = 4
    place.price_by_night = 200
    place.latitude = 40.7128
    place.longitude = -74.0060
    place.amenity_ids = ["amenity-1", "amenity-2"]

    def test_default_values(self):
        """test default value"""

        p = Place()
        self.assertEqual(p.name, "")
        self.assertEqual(p.city_id, "")
        self.assertEqual(p.user_id, "")
        self.assertEqual(p.description, "")
        self.assertEqual(p.number_rooms, 0)
        self.assertEqual(p.number_bathrooms, 0)
        self.assertEqual(p.max_guest, 0)
        self.assertEqual(p.price_by_night, 0)
        self.assertEqual(p.latitude, 0.0)
        self.assertEqual(p.longitude, 0.0)
        self.assertEqual(p.amenity_ids, "")

    def test_create_instance_without_kwargs(self):
        """
        create an instance of class without kwargs
        """
        self.assertIsInstance(self.place, Place)
        self.assertIsInstance(self.place, BaseModel)
        self.assertIsInstance(self.place.id, str)
        self.assertIsInstance(self.place.name, str)
        self.assertIsInstance(self.place.created_at, datetime)
        self.assertIsInstance(self.place.updated_at, datetime)
        self.assertIsInstance(self.place.city_id, str)
        self.assertIsInstance(self.place.user_id, str)
        self.assertIsInstance(self.place.description, str)
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertIsInstance(self.place.max_guest, int)
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertIsInstance(self.place.latitude, float)
        self.assertIsInstance(self.place.longitude, float)
        self.assertIsInstance(self.place.amenity_ids, list)

        self.assertEqual(self.place.name, "Luxury Apartment")
        self.assertEqual(self.place.id, "456-456-456")
        self.assertEqual(self.place.city_id, "city-123")
        self.assertEqual(self.place.user_id, "user-456")
        self.assertEqual(self.place.description, "A luxurious apartment")
        self.assertEqual(self.place.number_rooms, 3)
        self.assertEqual(self.place.number_bathrooms, 2)
        self.assertEqual(self.place.max_guest, 4)
        self.assertEqual(self.place.price_by_night, 200)
        self.assertEqual(self.place.latitude, 40.7128)
        self.assertEqual(self.place.longitude, -74.0060)
        self.assertEqual(self.place.amenity_ids, ["amenity-1", "amenity-2"])

    def test_create_instance_with_kwargs(self):
        """
        create an instance of class using kwargs
        """
        place_data = {
            "id": "891-891-891",
            "name": "Villa Retreat",
            "city_id": "city-456",
            "user_id": "user-789",
            "description": "A beautiful villa for a peaceful retreat",
            "number_rooms": 5,
            "number_bathrooms": 3,
            "max_guest": 8,
            "price_by_night": 300,
            "latitude": 34.0522,
            "longitude": -118.2437,
            "amenity_ids": ["amenity-3", "amenity-4"],
            "updated_at": "2023-08-11T23:00:25.886466",
            "created_at": "2023-08-11T23:00:25.886465"
        }

        new_place = Place(**place_data)
        self.assertIsInstance(new_place, Place)
        self.assertIsInstance(new_place, BaseModel)
        self.assertIsInstance(new_place.id, str)
        self.assertIsInstance(new_place.name, str)
        self.assertIsInstance(new_place.created_at, datetime)
        self.assertIsInstance(new_place.updated_at, datetime)
        self.assertIsInstance(new_place.city_id, str)
        self.assertIsInstance(new_place.user_id, str)
        self.assertIsInstance(new_place.description, str)
        self.assertIsInstance(new_place.number_rooms, int)
        self.assertIsInstance(new_place.number_bathrooms, int)
        self.assertIsInstance(new_place.max_guest, int)
        self.assertIsInstance(new_place.price_by_night, int)
        self.assertIsInstance(new_place.latitude, float)
        self.assertIsInstance(new_place.longitude, float)
        self.assertIsInstance(new_place.amenity_ids, list)

        self.assertEqual(new_place.id, "891-891-891")
        self.assertEqual(new_place.name, "Villa Retreat")
        self.assertEqual(new_place.city_id, "city-456")
        self.assertEqual(new_place.user_id, "user-789")
        self.assertEqual(new_place.description,
                         "A beautiful villa for a peaceful retreat")
        self.assertEqual(new_place.number_rooms, 5)
        self.assertEqual(new_place.number_bathrooms, 3)
        self.assertEqual(new_place.max_guest, 8)
        self.assertEqual(new_place.price_by_night, 300)
        self.assertEqual(new_place.latitude, 34.0522)
        self.assertEqual(new_place.longitude, -118.2437)
        self.assertEqual(new_place.amenity_ids, ["amenity-3", "amenity-4"])

    def test_to_dict(self):
        """ test to_dict class method """
        to_dic_return_dic = self.place.to_dict()
        expected_dic = self.place.__dict__.copy()
        expected_dic["__class__"] = self.place.__class__.__name__
        expected_dic["updated_at"] = self.place.updated_at.isoformat()
        expected_dic["created_at"] = self.place.created_at.isoformat()
        self.assertDictEqual(expected_dic, to_dic_return_dic)

    def test_save(self):
        """"
            test save class method
        """
        before_updated_time = self.place.updated_at
        self.place.name = "AMNA"
        self.place.save()
        after_updated_time = self.place.updated_at
        self.assertNotEqual(before_updated_time, after_updated_time)

    def test_str(self):
        """
            test str method

            check for string representaion
        """
        mn = self.place.__class__.__name__
        expected_str = f"[{mn}] ({self.place.id}) <{self.place.__dict__}>"
        self.assertEqual(self.place.__str__(), expected_str)
