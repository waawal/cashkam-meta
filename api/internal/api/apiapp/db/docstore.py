""" MongoDB Schemas"""

import datetime

from mongokit import Document, Connection

con = Connection()


class CashKameraBase(Document):

    structure = {'timestamp': datetime.datetime}
    default_values = {'timestamp': datetime.datetime.utcnow}


@con.register
class Ad(CashKameraBase):

    __database__ = 'ad_db'
    __collection__ = 'ads'

    structure = {
        'user': basestring,
        'text': basestring,
        'title': basestring,
        'active': bool,
        'coords': list,
        'region': list,
        'media': list,
        'storage': dict,
    }
    required_fields = ['user', 'media']
    default_values = {'active': False}


@con.register
class User(CashKameraBase):

    __database__ = 'user_db'
    __collection__ = 'users'

    structure = {
        'name': basestring,
        'subscription': bool,
        'active': bool,
        'email': basestring,
        'contact': {"address": basestring,
                     "city": basestring,
                     "phone": basestring,
                     "postalcode": basestring,
                     "name": basestring,
                     "country": basestring
                     },
        'storage': dict,
    }
    required_fields = ['name']
    default_values = {'subscription': False, 'active': True,}

ad = con.ad_db.ads.Ad
user = con.user_db.users.User
