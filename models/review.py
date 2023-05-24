#!/usr/bin/python3
""" creating a review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class that manages review objects"""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Instantiates a Review object"""
        super().__init__(*args, **kwargs)
