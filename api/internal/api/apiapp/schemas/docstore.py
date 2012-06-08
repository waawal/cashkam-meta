""" MongoDB Schemas"""

import datetime

from mongokit import Document


class CashKameraBase(Document):

    structure = {
        'timestamp' = datetime.datetime,
    }
    default_values = {'timestamp': datetime.datetime.utcnow}


class Ad(CashKameraBase):

    structure = {
        'user' = basestring,
        'text' = basestring,
        'active' = bool,
        'coords' = list,
        'region' = list,
        'media' = list,
        'storage' = dict,
    }
    required_fields = ['user', 'media']
    default_values = {'active': False}


class User(CashKameraBase):

    structure = {
        'name' = basestring,
        'subscription' = bool,
        'active' = bool,
        'contact' = {"address": basestring,
                     "city": basestring,
                     "phone": basestring,
                     "postalcode": basestring,
                     "name": basestring,
                     "email": basestring,
                     "country": basestring
                     },
        'storage' = dict,
    }
    required_fields = ['name']
    default_values = {'subscription': False, 'active': True,}
