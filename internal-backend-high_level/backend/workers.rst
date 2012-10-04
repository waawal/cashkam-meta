=======
Workers
=======

Model of the Publish Ad workerflow:


.. figure::  /_static/publish_ad.png

``Celery``

.. note::
  During Aplha: ``RQ``

Media Workers
-------------

``OpenCV`` for thumbnailification and POI discovery.

.. note::
  During Aplha: http://wiki.nginx.org/HttpImageFilterModule

Geospatial Workers
------------------

There are two categories of GEO=queus in CashKam;

1. ``new:ad`` = > when a new ad has been created.
2. ``update:pos`` = > when a device movement has been detected.

The ``new:ad`` queue looks for matches of the source against dynamic adlists. The ``update:pos`` looks through the users dynamic adlists after items matching the list=settings.

``Redis`` and ``MongoDB`` + Map/Reduce 

Maintenance Workers
-------------------

``MongoDB`` + Map/Reduce