
import inspect
from functools import wraps
from collections import Mapping

from bottle import HTTPError, request

import db

def requires_auth(f):
    """ Simple decorator checking for `token`in header and returning
        the username if the callback asked for it. if `token`is missing or
        invalid, a 401 is raised.
    """
    
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.get_header('token')
        if not token:
            raise HTTPError(401)
        else:
            username = db.key_store.check_auth(token)
            if not username:
                raise HTTPError(401)
            else:
                if 'authed' in inspect.getargspec(f)[0]:
                    kwargs['authed'] = username
                    return f(*args, **kwargs)
                else:
                    return f(*args, **kwargs)
    return wrapper

def validate_queries(reference):
    params = set(request.params.keys())
    if isinstance(reference, Mapping):
        reference = set(reference.keys())
    else:
        reference = set(reference)
    if params.issubset(reference):
        return True
    else:
        raise HTTPError(400)
