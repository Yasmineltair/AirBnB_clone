#!/usr/bin/python3
"""Review Class Definition"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class based on BaseModel """
    place_id = ""
    user_id = ""
    text = ""
