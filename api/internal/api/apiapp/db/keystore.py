""" The keystore backend, built with Redis """


import hashlib
import json

import redis


AUTH_PREFIX = "auth"
USERS_PREFIX = "users"

pool = redis.ConnectionPool()
con = redis.Redis(connection_pool=pool)

def auth_hash(username, password):
    """ Calculates the hash and returns it """
    token = ":".join((username, password))
    return hashlib.sha224(token).hexdigest()

def get_auth(username, password):
    """ Tries to get the authentication token."""
    authtoken = auth_hash(username, password)
    if con.get(":".join((AUTH_PREFIX, authtoken))) == username:
    return authtoken

def post_auth(username, password):
    """ Creates a hash token and sets a rediskey.
        A user is also created with a reference back to the hash.
    """
    authtoken = auth_hash(username, password)
    if con.setnx(":".join((USERS_PREFIX, username)), # Possibly better as a pipe
                 ":".join((AUTH_PREFIX, authtoken))):
        con.setnx(":".join((AUTH_PREFIX, authtoken)), username)
        return authtoken
    return False

def put_auth(username, password, newPassword):
    """ Updates auth keys. """
    authtoken = auth_hash(username, password)
    newauthtoken = auth_hash(username, newPassword)
    if con.set(":".join((USERS_PREFIX, username)), # Possibly better as a pipe
               ":".join((AUTH_PREFIX, newauthtoken))):
        return con.rename(":".join((AUTH_PREFIX, authtoken)),
                          ":".join((AUTH_PREFIX, newauthtoken)))
    return False

def check_auth(token):
    return con.get(":".join((AUTH_PREFIX, token)))

