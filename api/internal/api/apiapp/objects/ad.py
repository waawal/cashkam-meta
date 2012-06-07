""" Returns dicts representing the objects. """

def User(name, subscription=False, active=True, contact=None, storage=None):
    """ Returns a dict representing a user. """
    if contact is None:
        contact = {"address": None,
                   "city": None,
                   "phone": None,
                   "postalcode": None,
                   "name": None,
                   "email": None,
                   "country": None}
    user = dict(name=name, subscription=subscription, active=active,
                contact=contact, storage=storage)
    return user
