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
    app.route('/ad', method=['GET'], callback=ad.get_ad)
    app.route('/ad', method=['PUT'], callback=ad.put_ad)
    app.route('/ad', method=['DELETE'], callback=ad.del_ad)
    
    app.route('/ads', method=['GET'], callback=ad.get_ads)
    app.route('/ads', method=['POST'], callback=ad.post_ads)
    
    app.route('/auth', method=['GET'], callback=auth.get_auth)
    app.route('/auth', method=['POST'], callback=auth.post_auth)
    app.route('/auth', method=['PUT'], callback=auth.put_auth)
    
    app.route('/user', method=['GET'], callback=user.get_user)
    app.route('/user', method=['PUT'], callback=user.put_user)
    
    app.route('/user', method=['DELETE'], callback=user.del_user)
    app.route('/users', method=['GET'], callback=users.get_users)
    app.route('/users', method=['POST'], callback=users.get_users)

app = Bottle()
setup_routing(app)
