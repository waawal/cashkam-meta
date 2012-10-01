=======
Backend
=======

API Endpoints
-------------

.. figure::  _static/backend_drawing.png

The Endpoint architecture runs exclusively on Ubuntu 12.04. It consists of a multiprocess pre-forked WSGI-app on coro-steroids (gevent) communicating over a unified REST-interface with all the frontends.

Router
~~~~~~

NGINX routes based on subdomains to the correct port set up in CIRCUS.

Load Balancing
~~~~~~~~~~~~~~

NGINX (+ DNS round robin and CARP for HA)

Workers
-------

``Celery`` or ``RQ``  

Media Workers
~~~~~~~~~~~~~

``OpenCV`` for thumbnailification and POI discovery.

Geo Workers
~~~~~~~~~~~

``Redis`` and ``MongoDB`` Map/Reduce 

Maintenance Workers
~~~~~~~~~~~~~~~~~~~

``MongoDB`` + Map/Reduce

Sessions
--------

Sessions are stored in ``Redis``hashes.

Streaming
~~~~~~~~~

Streaming of data to sessions is achieved by the implementation of two technologies. On the app-side we use secure ``websockets`` and in the webbrowser we use ``ServerEvents``since we don't need the duplexed communication.

Data Storage
------------

Static files served over HTTP with ``NGINX``.

Geographical Queries
~~~~~~~~~~~~~~~~~~~~

``Elastic Search`

Media
~~~~~

``NGINX``

Users
~~~~~

``MongoDB`

Ads
~~~

``MongoDB``