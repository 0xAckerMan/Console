#!/usr/bin/python3
'''
The base model
'''
import uuid
from datetime import datetime


class BaseModel:
    '''
    The class implementation
    '''

    def __init__(self) -> None:
        id = str(uuid.uuid4())
        created_at = datetime.now()
        updated_at = datetime.now()

    def __str__(self) -> str:
        
