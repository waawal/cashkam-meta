.. figure::  _static/massforstroelse-logo.png

========================================
CashKamera High Level Technical Overview
========================================
:Info: See the `docs repository <https://github.com/waawal/cashkam-meta>`_ for the latest source.
:Author: Daniel Waardal

This is the internal documentation of the inner workings of the CashKam platform.

.. figure::  _static/client-backend_drawing.png

Clients (Frontends)
-------------------

The clients are not tied down to a specific platform. A client for CashKam can be implemented for all platforms that supports TCP-sockets (a HTTP-library is of course very nice to have).

Overview
~~~~~~~~

.. toctree::
   :maxdepth: 3
   
   frontend/mobile
   frontend/web

Engine (Backend)
----------------

The engine is a umberella term for all things backend. Everything that lives on a server can be found here besides the distribution-nodes of static files and media.

Overview
~~~~~~~~

.. toctree::
   :maxdepth: 3

   backend/endpoints
   backend/workers
   backend/sessions
   backend/db
   backend/statics