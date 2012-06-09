""" The main WSGI-app """

import json

from bottle import (get,
                    post,
                    put,
                    delete,
                    request,
                    )

import db
