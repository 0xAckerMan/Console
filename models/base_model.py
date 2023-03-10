#!/usr/bin/python3
'''
The base model
'''
import uuid
from datetime import datetime
import models


class BaseModel:
    '''
    The class implementation
    '''

    def __init__(self, *args, **kwargs):

        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            kwargs["created_at"] = datetime.strptime(
                kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f"
            )
            kwargs["updated_at"] = datetime.strptime(
                kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f"
            )

            for key, value in kwargs.items():
                if "__class__" not in key:
                    setattr(self, key, value)

    def __str__(self):
        return (
            f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")
    
    def save(self):
        '''Updates the save time'''

        updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''Returns a dictionary representation of base model'''

        dict_repr = dict(self.__dict__)
        dict_repr["__class__"] = self.__class__.__name__
        dict_repr['created_at'] = self.created_at.strftime(
            "%Y-%m-%dT%H:%M:%S.%f"
        )
        dict_repr['updated_at'] = self.updated_at.isoformat()

        return dict_repr