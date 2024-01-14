#!/usr/bin/python3
"""BaseModel class Definition"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """ BASE MODEL class """
    iso_format = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """ init class instances """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if kwargs:
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = \
                        datetime.strptime(val, self.iso_format)
                else:
                    self.__dict__[key] = val
        else:
            models.storage.new(self)

    def __str__(self):
        """ str representation of class """
        return "[{}] ({}) {}".\
            format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ update instance (not yet implemented) """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ converts instance to dict """
        out_dict = self.__dict__.copy()
        out_dict['created_at'] = self.created_at.isoformat()
        out_dict['updated_at'] = self.updated_at.isoformat()
        out_dict['__class__'] = self.__class__.__name__
        return out_dict
