Main Objects
============

`JSON`-notated objects returned by some of the API methods.

User Object
-----------

:http:get:`/user/(str:name)`, :http:get:`/users`

.. js:class:: User

   A object representing a user.

.. js:data:: User.name

   The Username in utf-8.

.. js:data:: User.subscription

   Status for subscription service.  
   
.. code-block:: javascript

   true or false
   
.. js:data:: User.active

   Set to false when user has requested to be removed.  
   
.. code-block:: javascript

   true or false
   
.. js:data:: User.contact

   Contact details for user.  

.. code-block:: javascript

   {"address": "Kattvägen 7",
    "city": "Mjau",
    "phone": "08-12332101",
    "postalcode": "54230",
    "name": "Herr Katt",
    "email": "katt@katt.mjau",
    "country": "Kattlandet"}
   
.. js:data:: User.storage

   Misc keystore.

Ad Object
---------

:http:get:`/ads`, :http:get:`/ad/(str:id)`

.. js:class:: Ad

   A object representing a ad.

.. js:data:: Ad.id
   
   The id of the ad.

.. js:data:: Ad.user
   
   Published by :js:data:`User.name`

.. js:data:: Ad.text
   
   The ad text.

.. js:data:: Ad.active
   
   True if the ad is active.

.. code-block:: javascript

   true or false
   
.. js:data:: Ad.datetime
   
   When the ad was published (UTC)
   
.. js:data:: Ad.coords
   
   Coordinates.  
   
.. code-block:: javascript

   [1.51353, 0.14345]

.. js:data:: Ad.region

   Region based on coords.  

.. code-block:: javascript

   ["countrycode", "region", "city"]

.. js:data:: Ad.media

   Images
   
   * Square
   * small
   * normal
   * original

.. code-block:: javascript

   [["url", "url", "url", "url"]["url", "url", "url", "url"]]

.. js:data:: Ad.storage

   Misc keystore.

Other Objects
=============

Error Object
------------

.. js:class:: Error()

   Generic Error message

.. js:data:: Error.message
   
   The error message in utf-8

.. js:data:: Error.code

   Error code.

GenericResponse Object
----------------------

.. js:class:: GenericResponse()

   Generic Response

.. js:data:: GenericResponse.response
   
   Response to be parsed as JSON

