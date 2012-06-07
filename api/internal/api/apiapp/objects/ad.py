""" Returns a mapping representing the objects. """


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
        storage = []
    user = dict(name=name, subscription=subscription, active=active,
                contact=contact, storage=storage)
    return user

def Ad(user=None, text=None, active=False, datetime=None, coords=None,
       region=None, media=None, storage=None):
    """ Returns a mapping representing a ad. """
    
