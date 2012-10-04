===============
Web Application
===============

The web application uses the standard API-endpoints. It is built as a single-page web application with a design that resembles Pinterest [#f1]_ to a certain extent.

Stack
-----

Javascript (Coffeescript)
~~~~~~~~~~~~~~~~~~~~~~~~~

The application is written with ``Coffeescript`` and compiled to ``Javascript``.

MVC
  ``Spine.js`` by Alex Maccaw has been choosen to serve as the MVC-framework. The rationale is that Spine is written in coffeescript and that it needs very little boiler plate code in order to efficiently make use of our REST-like backend. It is also very convenient to build the app with ``Coffeescript`` classes. 

Map
  We use the excellent ``Leaflet`` project to present map-tiles.

Ad positioning
  To achieve a "Pinterest"-effect we turn to ``Masonry``. ``Wookmark`` [#f2]_ was previously considered due to its relative lightness compared to ``Masonry``, however it was unfortunately not flexible enough.


*Dependencies:*

* `Spine <http://spinejs.com/>`_
* `JQuery <http://jquery.com/>`_
* `JQueryUI <http://jqueryui.com/>`_
* `Masonry <http://masonry.desandro.com/>`_
* `Leaflet <http://leaflet.cloudmade.com/>`_

Styling/Layout
~~~~~~~~~~~~~~

The stylesheets are using the ``Stylus`` preprocessor together with the ``nib`` mixins. This choice was made after looking at solutions such as ``SASS`` + ``Compass`` [#f3]_ , however, the syntax of ``Stylus`` allows for less boilerplate code. In addition we could expand our use of ``Stylus`` in the future to handle styling of other client-implementations.

*Dependencies:*

* `Stylus <http://learnboost.github.com/stylus/>`_
* `nib <http://visionmedia.github.com/nib/>`_


.. rubric:: Footnotes

.. [#f1] http://pinterest.com/
.. [#f2] http://www.wookmark.com/jquery-plugin
.. [#f3] http://compass-style.org/