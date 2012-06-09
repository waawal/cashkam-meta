
import db.keystore


def get_auth():
    result = db.keystore.get_auth(username, password)
    if result:
        return result
    else:
        raise # TODO: HTTP Error

def post_auth():
    pass

def put_auth(username):
    pass
