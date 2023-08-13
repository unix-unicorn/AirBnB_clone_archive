"""Unittest for base model
"""
import unittest
from models.state import State
from models.base_model import BaseModel
from models import storage
from datetime import datetime


class TestConstructor(unittest.TestCase):
    """
    test class for the max_integer() function.
    """
    state = State()
    state.name = "Cairo"

    def test_create_instance_without_kwargs(self):
        """
        create an instance of class without kwargs
        """
        self.assertIsInstance(self.state, State)
        self.assertIsInstance(self.state, BaseModel)
        self.assertIsInstance(self.state.id, str)
        self.assertIsInstance(self.state.created_at, datetime)
        self.assertIsInstance(self.state.updated_at, datetime)
        self.assertIsInstance(self.state.name, str)
        self.assertEqual(self.state.name, "Cairo")

    def test_create_instance_with_kwargs(self):
        """
        create an instance of class using kwargs
        """
        state_data = {
            "id": "AMNA-803",
            "name": "Alex",
            "created_at": "2023-08-11T23:00:25.886465",
            "updated_at": "2023-08-11T23:00:25.886466"
        }

        new_state = State(**state_data)

        self.assertIsInstance(new_state, State)
        self.assertIsInstance(new_state, BaseModel)
        self.assertIsInstance(new_state.id, str)
        self.assertIsInstance(new_state.created_at, datetime)
        self.assertIsInstance(new_state.updated_at, datetime)
        self.assertIsInstance(new_state.name, str)

        self.assertEqual(new_state.id, "AMNA-803")
        self.assertEqual(new_state.name, "Alex")

    def test_to_dict(self):
        """
            test to_dict class method
        """
        to_dict_returned_dict = self.state.to_dict()
        expected_dict = self.state.__dict__.copy()
        expected_dict["__class__"] = self.state.__class__.__name__
        expected_dict["updated_at"] = self.state.updated_at.isoformat()
        expected_dict["created_at"] = self.state.created_at.isoformat()
        self.assertDictEqual(expected_dict, to_dict_returned_dict)

    def test_save(self):
        """"
            test save class method
        """
        before_update_time = self.state.updated_at
        self.state.name = "giza"
        self.state.save()
        after_update_time = self.state.updated_at
        self.assertNotEqual(before_update_time, after_update_time)

    def test_str(self):
        """
            test str method

            check for string representaion
        """
        n = self.state.__class__.__name__
        expected_str = f"[{n}] ({self.state.id}) <{self.state.__dict__}>"
        self.assertEqual(self.state.__str__(), expected_str)
