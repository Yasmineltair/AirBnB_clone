#!/usr/bin/python3
""" contain BaseModel class """
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ main class"""

    def __init__(self, *args, **kwargs):
        """ init method """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        iso_format = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) >= 1:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict___[key] = datetime
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """ str representation of the BaseModel instances"""
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """  updates the attribute updated_at with the current datetime"""
        self.updated_at = datetime.today()

    def to__dict(self):
        """ returns a dictionary containing keys/values of the instance"""
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
