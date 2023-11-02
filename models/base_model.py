#!/usr/bin/python3
import uuid
from datetime import datetime
'''This is the module for BaseModel Class'''


class BaseModel:
    def __init__(self, *args, **kwargs):
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "created_at":
                    self.created_at = value
                elif key == "updated_at":
                    self.updated_at = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def save(self):
        self.updated_at = datetime.now()

    def __str__(self):
        """Magic method str,
        print the actual size of the rectangle.
        """
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        new_dict = self.__dict__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
