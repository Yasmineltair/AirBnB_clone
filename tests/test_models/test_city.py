#!/usr/bin/python3
""" testing for city class"""
import models
from models.city import City
import unittest
import os


class test_city(unittest.TestCase):
    """ unittest for city class"""
    def test_state_id(self):
        """ test state_id"""
        self.assertEqual(str, type(City.state_id))

    def test_name(self):
        """ test name"""
        self.assertEqual(str, type(City.name))


if __name__ == "__main__":
    unittest.main()
