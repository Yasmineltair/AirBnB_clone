#!/usr/bin/python3
""" testing for state class"""
import models
from models.state import State
import unittest
import os


class test_state(unittest.TestCase):
    """ unittest for state class"""
    def test_name(self):
        """ test email"""
        self.assertEqual(str, type(State.name))


if __name__ == "__main__":
    unittest.main()
