""" The keystore backend, built with Redis """

import json

import redis

con = redis.ConnectionPool()

def get_auth(username, password):
    pass

def post_auth(username, password):
    pass

def put_auth(name, password, newPassword):
    pass
