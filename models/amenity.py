#!/usr/bin/python3
"""

    amenity inheritance
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
        Class to represent an 'Amenity' object
        An instance of this class represents a single amenity,
        with a name attribute
        Attributes:
            name (str): name of the amenity
    """
    name = ""
