#!/usr/bin/python3
""" testing for place class"""
import models
from models.place import Place
import unittest
import os


class test_place(unittest.TestCase):
    """ unittest for place class"""
    def test_city_id(self):
        """ test city id"""
        self.assertEqual(str, type(Place.city_id))

    def test_user_id(self):
        """ test user id"""
        self.assertEqual(str, type(Place.user_id))

    def test_name(self):
        """ test name"""
        self.assertEqual(str, type(Place.name))

    def test_description(self):
        """ test description"""
        self.assertEqual(str, type(Place.description))

    def test_number_rooms(self):
        """ test number of rooms"""
        self.assertEqual(int, type(Place.number_rooms))

    def test_number_bathrooms(self):
        """ test number of bathrooms"""
        self.assertEqual(int, type(Place.number_bathrooms))

    def test_max_guest(self):
        """ test max of guests"""
        self.assertEqual(int, type(Place.max_guest))

    def test_price_by_night(self):
        """ test price_by_night"""
        self.assertEqual(int, type(Place.price_by_night))

    def test_latitude(self):
        """ test latitude"""
        self.assertEqual(float, type(Place.latitude))

    def test_longitude(self):
        """ test longitude"""
        self.assertEqual(float, type(Place.longitude))

    def test_amenity_ids(self):
        """ test amenity_ids"""
        self.assertEqual(list, type(Place.amenity_ids))


if __name__ == "__main__":
    unittest.main()
