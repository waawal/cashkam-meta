============
Data Storage
============

The document-like data is stored in ``CouchDB`` [#f1]_ . ``MongoDB`` [#f2]_ was evaluated and was under a long time in favour because of its builtin geospatial abilities, however, after the introduction of ``Elastic Search`` to the stack ``MongoDB`` was scrapped due to the relative ease to keep master-master ``CouchDB`` instances in sync over WAN.

Users
-----

``CouchDB``

Ads
---

``CouchDB``

Archiving
---------

A separate instance of ``CouchDB``.


.. rubric:: Footnotes

.. [#f1] http://couchdb.apache.org/
.. [#f2] http://www.mongodb.org/