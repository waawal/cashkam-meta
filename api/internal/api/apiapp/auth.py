
from bottle import HTTPError

import db
from utils import requires_auth, validate_queries


def get_auth():
    validate_queries(['name','password'])
    result = db.keystore.get_auth(username, password)
    if result:
        return result
    else:
        raise HTTPError(401, "Authentication Failed.")

def post_auth():
    result = db.keystore.post_auth(username, password)
    if result:
        return result
    else:
        raise HTTPError(409, "Username already in use.")

@requires_auth
def put_auth(username, password, newpassword):
    result = db.keystore.put_auth(username, password, newpassword)
    if result:
        return result
    else:
        raise HTTPError(404, "Username not found.")
