
from bottle import HTTPError

import db
from utils import requires_auth, validate_queries


def get_user(name):
    validate_queries('name')
    try:
        return db.doc_store.user.one({'name':name}).to_json()
    except:
        raise HTTPError(404)

@requires_auth
def put_user(name, authed):
    pass

@requires_auth
def del_user(name, authed):
    validate_queries('name')
    pass

