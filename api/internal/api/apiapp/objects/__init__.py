""" MongoDB Schemas"""

import datetime

from mongokit import Document

#import ad
#import user
#import response


class Ad(Document):

    structure = {
        user = basestring,
        text = basestring,
        active = bool,
        timestamp = datetime.datetime,
        coords = list
        region = list
        media = list
        storage = dict
    }
    required_fields = ['user', 'media']
    #default_values = ad.AD_TEMPLATE


class User(Document):

    structure = {
        'name' = basestring,
        'subscription' = bool,
        'active' = bool,
        'contact' = dict,
        'storage' = dict,
    }
    required_fields = ['name']
    #default_values = user.USER_TEMPLATE
