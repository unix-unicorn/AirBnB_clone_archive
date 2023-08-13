#!/usr/bin/python3
"""Unittest for base model
"""
import unittest
from models.user import User
from models.base_model import BaseModel
from models import storage
from datetime import datetime
class TestAmna(unittest.TestCase):
    """
    test class for the max_integer() function.
    """
    email = "amnataha2011@gmail.com"
    password = "A12345"
    first_name = "Amna"
    last_name = "Taha"
    def Test_the_same(self):
        A = User()
        self.assertEquall(A.email, "")
        self.assertEquall(A.password, "")
        self.assertEquall(A.first_name, "")
        self.assertEquall(A.last_name, "")
    def Test_without_args(self):
        """my function test without args"""
        self.assertInstance(self.user, User)
        self.assertInstance(self.user, BaseModel)
        self.assertInstance(self.user.id, str)
        self.assertInstance(self.user.created_at, datetime)
        self.assertIsInstance(self.user.updated_at, datetime)
        self.assertInstance(self.user.email, str)
        self.assertInstance(self.user.password, str)
        self.assertInstance(self.user.first_name, str)
        self.assertInstance(self.user.last_name, str)
        self.assertEqual(self.user.email, "amnataha2011@gmail.com")
        self.assertEqual(self.user.password, "A12345")
        self.assertEqual(self.user.first_name, "Amna")
        self.assertEqual(self.user.last_name, "Taha")
    def Test_with_args(self):
        "my args test function"""
        f_all = {
            "id": "user-891",
            "email": "amna@gmail.com",
            "password": "ana123",
            "first_name": "rayan",
            "last_name": "ayman",
            "created_at": "2023-08-11T23:00:25.886465",
            "updated_at": "2023-08-11T23:00:25.886466"
        }
        A_user= User(**f_all)
        self.assertInstance(A_user, User)
        self.assertInstance(A_user, BaseModel)
        self.assertInstance(A_user.id, str)
        self.assertInstance(A_user.created_at, datetime)
        self.assertIsInstance(A_user.updated_at, datetime)
        self.assertInstance(A_user.email, str)
        self.assertInstance(A_user.password, str)
        self.assertInstance(A_user.first_name, str)
        self.assertInstance(A_user.last_name, str)
        self.assertEqual(A_user.id, "user-891")
        self.assertEqual(A_user.email, "amna@gmail.com")
        self.assertEqual(A_user.password, "ana123")
        self.assertEqual(A_user.first_name, "rayan")
        self.assertEqual(A_user.last_name, "ayman")
    def test_to_dict(self):
        """
            test to_dict class method
        """
        to_dict_returned_dict = self.user.to_dict()
        expected_dict = self.user.__dict__.copy()
        expected_dict["__class__"] = self.user.__class__.__name__
        expected_dict["updated_at"] = self.user.updated_at.isoformat()
        expected_dict["created_at"] = self.user.created_at.isoformat()
        self.assertDictEqual(expected_dict, to_dict_returned_dict)

    def test_save(self):
        """"
            test save class method
        """
        before_update_time = self.user.updated_at
        self.user.email = "updated@example.com"
        self.user.save()
        after_update_time = self.user.updated_at
        self.assertNotEqual(before_update_time, after_update_time)

    def test_str(self):
        """
            test str method

            check for string representaion
        """
        n = self.user.__class__.__name__
        expected_str = f"[{n}] ({self.user.id}) <{self.user.__dict__}>"
        self.assertEqual(self.user.__str__(), expected_str)
