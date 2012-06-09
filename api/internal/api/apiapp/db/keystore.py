""" The keystore backend, built with Redis """


import hashlib
import json

import redis


AUTH_PREFIX = "auth"
USERS_PREFIX = "users"

con = redis.ConnectionPool()

def auth_hash(username, password):
    """ Calculates the hash and returns it """
    token = ":".join((username, password))
    return hashlib.sha512(token).hexdigest()

def get_auth(username, password):
    """ Tries to get the authentication token, if it fail, it raises a
        HTTPError 401.
    """
    authtoken = auth_hash(username, password)
    result = con.get(":".join((AUTH_PREFIX, authtoken)))
    return result

def post_auth(username, password):
    """ Creates a hash token and sets a rediskey.
        A user is also created with a reference back to the hash.
    """
    authtoken = auth_hash(username, password)
    if con.setnx(":".join((USERS_PREFIX, username)),
                 ":".join((AUTH_PREFIX, authtoken))):
        result = con.setnx(":".join((AUTH_PREFIX, authtoken)), username)
        return result
    return False

def put_auth(name, password, newPassword):
    authtoken = auth_hash(name, password)
    newauthtoken = auth_hash(name, newPassword)
    result = con.renamenx(":".join((AUTH_PREFIX, authtoken)),
                          ":".join((AUTH_PREFIX, newauthtoken)))
    return result
