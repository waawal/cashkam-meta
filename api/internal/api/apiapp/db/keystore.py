""" The keystore backend, built with Redis """


import hashlib
import json

import redis


AUTH_PREFIX = "auth"

con = redis.ConnectionPool()

def auth_hashed(username, password):
    """ Calculates the hash and returns it """
    token = ":".join((username, password))
    return hashlib.sha512(token).hexdigest()

def get_auth(username, password):
    """ Tries to get the authentication token, if it fail, it raises a
        HTTPError 401.
    """
    authtoken = auth_hash(username, password)
    result = con.get(":".join((AUTH_PREFIX, authtoken)))
    if result:
        return result
    else:
        # Raise

def post_auth(username, password):
    pass

def put_auth(name, password, newPassword):
    pass
