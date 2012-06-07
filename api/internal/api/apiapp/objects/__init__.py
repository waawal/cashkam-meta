import datetime

from mongokit import Connection, Document

import ad
import user
import response

mongo = Connection()

@mongo.register
class Ad(Document):
    structure = ad.AD_TEMPLATE


@mongo.register
class User(Document):
    structure = user.USER_TEMPLATE
