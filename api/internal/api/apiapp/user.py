
from bottle import HTTPError

import db
from utils import requires_auth, validate_queries


def get_user(name):
    validate_queries('name')
    try:
        return db.doc_store.user.one({'name':name}).to_json()
    except: # TODO: Bug! one raises exception if > 1
        raise HTTPError(404, "user_not_found")

@requires_auth
def put_user(name, authed):
    r = validate_queries(db.doc_store.User.structure)
    if name == authed:
        user = db.doc_store.user.one({'name':name})
        if not user:
            raise HTTPError404
        user.update(r)
        return user.save()
    
    raise HTTPError(403)

@requires_auth
def del_user(name, authed):
    validate_queries('name')
    # TODO: Deactivate User and remove auth
    pass

