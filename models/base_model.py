#!/usr/bin/python3
"""
Create the BaseModel class
"""


from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
"""
BaseModel class for unique ids
"""
    def __init__(self):
        """
        BaseModel Constructor
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def save(self):
        """
        Update with the current time
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Instance dictionary
        """
        data = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        data['created_at'] = self.created.at.isoformat()
        data['updated_at'] = self.update_at.isoformat()

        return data

        
