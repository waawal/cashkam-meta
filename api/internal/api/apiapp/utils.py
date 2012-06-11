
import inspect
from functools import wraps

from bottle import HTTPError, request

import db

def requires_auth(f):
    """ Simple decorator checking for `token`in header and returning
        the username if the callback asked for it. if `token`is missing or
        invalid, a 401 is raised.
    """
    def wrapper(*args, **kwargs)
        token = request.headers.get('token')
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
