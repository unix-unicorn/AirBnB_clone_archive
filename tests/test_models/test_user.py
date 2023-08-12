#!/usr/bin/python3
"""Unittest for base model
"""
import unittest
from models.user import User
from models.base_model import BaseModel
from models import storage
from datetime import datetime
class TestConstructor(unittest.TestCase):
    """
    test class for the max_integer() function.
    """
