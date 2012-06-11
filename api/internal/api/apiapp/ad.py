
from bottle import HTTPError

import db
from utils import requires_auth


def get_ad(adid):
    pass

@requires_auth
def put_ad(adid, authed):
    pass

@requires_auth
def del_ad(adid, authed):
    pass
