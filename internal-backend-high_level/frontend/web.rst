Web Application
===============

The web application uses the standard API-endpoints. It is built as a single-page web application with a design that resembles pinterest to a certain extent.

Stack
-----

Javascript (Coffeesript)
~~~~~~~~~~~~~~~~~~~~~~~~

``Spine.js`` by Alex Maccaw has been choosen to serve as the MVC-framework. The rationale is that Spine is written in coffeescript and that it needs very little boiler plate code in order to efficiently make use of our REST-like backend.

*Dependencies:*

* `Spine.js <http://spinejs.com/>`_
* `JQuery <http://jquery.com/>`_
* `JQueryUI (for draggables and droppables) <http://jqueryui.com/>`_
* `Masonry (for the pinterest-layout) <http://masonry.desandro.com/>`_

Layout
~~~~~~

The stylesheets are using the ``Stylus`` preprocessor together with the ``nib`` mixins. This choice was made after looking at solutions such as SASS + Compass, however, the syntax of ``Stylus`` allows for less boilerplate code. In addition we could expand our use of ``Stylus`` in the future to handle styling of other implementations of clients.

*Dependencies:*

* `Stylus <http://learnboost.github.com/stylus/>`_
* `nib <http://visionmedia.github.com/nib/>`_