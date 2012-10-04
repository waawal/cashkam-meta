=============
API Endpoints
=============

.. figure::  /_static/backend_drawing.png

The Endpoint architecture runs exclusively on Ubuntu 12.04. It consists of a multiprocess pre-forked WSGI-app on coro-steroids (``gevent``) communicating over a unified REST-interface with all the frontends.

Router
------

``NGINX`` routes based on subdomains to the correct port set up in ``CIRCUS``.

Load Balancing
--------------

``NGINX`` (+ DNS round robin and ``CARP`` for HA)