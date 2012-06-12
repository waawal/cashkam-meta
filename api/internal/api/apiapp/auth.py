
from bottle import HTTPError

import db
from utils import requires_auth, validate_queries


def get_auth():
    r = validate_queries(['name','password'])
    result = db.key_store.get_auth(r['name'], r['password'])
    if result:
        return result
    else:
        raise HTTPError(401, "Authentication Failed.")

def post_auth():
    r = validate_queries(['name','password'])
    result = db.key_store.post_auth(r['name'], r['password'])
    if result: # TODO: Should create a new User()
        return result
    else:
        raise HTTPError(409, "Username already in use.")

@requires_auth
def put_auth(name, authed):
    r = validate_queries(['password', 'newPassword'])
    if name == authed:
        result = db.key_store.put_auth(name, r['password'], r['newPassword'])
        if result:
            return result
        else:
            raise HTTPError(404, "Username not found.")
    else:
        raise HTTPError(403)
