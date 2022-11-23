#!/usr/bin/python3
""" A super class model
"""
import uuid
from datetime import datetime
import models

class BaseModel:
    """ A base model class that defines
    all common attributes and methods
    """

    def __init__(self, *args, **kwargs):
        """ Initializes """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
        else:
            f = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(kwargs[key], f)
                if key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        """ A str doc """
        class_name = "[" + self.__class__.__name__+"]"
        dct = {k: v for (k, v) in self.__dict__.items() if (not v) is False}
        return class_name + " (" + self.id + ") " + str(dct)

    def save(self):
        """ A public instance method that updates "updated_at"
        with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ A public instance method that creates a dict, adds a key
        and return the datetime in str"""

        new_dict = {}

        for keys, values in self.__dict__.items():  # Iterating through dict
            if key == "created_at" or key == "updated_at":
                new_dict[key] = value.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                if not values:
                    pass
                else:
                    new_dict[key] = values
        new_dict['__class__'] = self.__class__.__name__

        return new_dict
