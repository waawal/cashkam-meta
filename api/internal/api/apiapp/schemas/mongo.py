""" MongoDB Schemas"""

import datetime

from mongokit import Document


class Ad(Document):

    structure = {
        'user' = basestring,
        'text' = basestring,
        'active' = bool,
        'timestamp' = datetime.datetime,
        'coords' = list,
        'region' = list,
        'media' = list,
        'storage' = dict,
    }
    required_fields = ['user', 'media']
    default_values = {'timestamp': datetime.datetime.utcnow}


class User(Document):

    structure = {
        'name' = basestring,
        'subscription' = bool,
        'active' = bool,
        'contact' = dict,
        'storage' = dict,
        'created' = datetime.datetime,
    }
    required_fields = ['name']
    default_values = {'subscription': False, 'active': True,
                      'created': datetime.datetime.utcnow}
