
from bottle import HTTPError

import db
from utils import requires_auth


def get_user(username):
    pass

@requires_auth
def put_user(username, authed):
    pass

@requires_auth
def del_user(username, authed):
    pass

