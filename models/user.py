#!/usr/bin/python3
''' creates a user from the basemodel'''

from models import base_model


class User(base_model):
    '''Class implementation'''

    email = ''
    password = ''
    first_name = ''
    last_name = ''