""" Returns a mapping representing the objects. """


AD_TEMPLATE = dict(
id = None,
user = None,
text = None,
active = False,
timestamp = None,
coords = []
region = []
media = []
storage = {}
)

def Ad(user=None, text=None, active=False, timestamp=None, coords=None,
       region=None, media=None, storage=None):
    """ Returns a mapping representing a ad. """
    pass
