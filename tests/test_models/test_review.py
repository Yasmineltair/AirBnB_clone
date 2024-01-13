#!/usr/bin/python3
""" testing for review class"""
import models
from models.review import Review
import unittest
import os


class test_review(unittest.TestCase):
    """ unittest for class review"""
    def test_place_id(self):
        """ test place id"""
        self.assertEqual(str, type(Review.place_id))

    def test_user_id(self):
        """ test user_id"""
        self.assertEqual(str, type(Review.user_id))

    def test_text(self):
        """ test text"""
        self.assertEqual(str, type(Review.text))


if __name__ == "__main__":
    unittest.main()
