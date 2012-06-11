""" The main WSGI-app """

import json

import bottle


import db

import ad
import ads

import auth

import user
import users

def setup_routing(app):
    """ Routing. """
    app.route('/ad', method=['GET'], ad.get_ad)
    app.route('/ad', method=['PUT'], ad.put_ad)
    app.route('/ad', method=['DELETE'], ad.del_ad)
    
    app.route('/ads', method=['GET'], ad.get_ads)
    app.route('/ads', method=['POST'], ad.post_ads)
    
    app.route('/auth', method=['GET'], auth.get_auth)
    app.route('/auth', method=['POST'], auth.post_auth)
    app.route('/auth', method=['PUT'], auth.put_auth)
    
    app.route('/user', method=['GET'], user.get_user)
    app.route('/user', method=['PUT'], user.put_user)
    
    app.route('/user', method=['DELETE'], user.del_user)
    app.route('/users', method=['GET'], users.get_users)
    app.route('/users', method=['POST'], users.get_users)

app = Bottle()
setup_routing(app)
