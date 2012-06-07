""" Returns a mapping representing the objects. """


USER_TEMPLATE = dict(
name = None,
subscription = None,
active = False,
contact = {},
storage = {},
)

def User(name=None, subscription=False, active=True,
         contact=None, storage=None):
    """ Returns a mapping representing a user. """
    if contact is None:
        contact = {"address": None,
                   "city": None,
                   "phone": None,
                   "postalcode": None,
                   "name": None,
                   "email": None,
                   "country": None}
    if storage is None:
        storage = {}
    user = dict(name=name, subscription=subscription, active=active,
                contact=contact, storage=storage)
    return user
