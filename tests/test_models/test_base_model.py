#!/usr/bin/python3
"""Unitest for base_model
"""
import unittest
from models.base_model import BaseModel
import datetime


class TestBaseModel(unittest.testcase):
    """
    Class for testing base model case
    """

    my_model = BaseModel()

    def test_BaseModel(self):
        """ Base model instances and attributes
        test case
        """
