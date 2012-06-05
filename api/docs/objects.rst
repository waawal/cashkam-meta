Main Objects
============

`JSON`-notated objects returned by some of the API methods.

UserObject
----------

:http:get:`/user/(str:id)`, :http:get:`/users`

.. js:class:: UserObject

   A object representing a user.

.. js:data:: UserObject.id
   
   The user id.

.. js:data:: UserObject.username

   The Username in utf-8.

.. js:data:: UserObject.subscription

   Status for subscription service.  
   
.. code-block:: javascript

   true or false

.. js:data:: UserObject.contact

   Contact details for user.  

.. code-block:: javascript

   {"address": "Kattvägen 7", "city": "Mjau", "phone": "08-12332101", "postalcode": "54230", "name": "Herr Katt", "email": "katt@katt.mjau", "country": "Kattlandet"}
   
.. js:data:: UserObject.settings

   Misc keystore.

AdObject
--------

:http:get:`/ads`, :http:get:`/ad/(str:id)`

.. js:class:: AdObject

   A object representing a ad.

.. js:data:: AdObject.id
   
   The id of the ad.

.. js:data:: AdObject.user
   
   Published by :js:data:`UserObject.id`

.. js:data:: AdObject.text
   
   The ad text.

.. js:data:: AdObject.active
   
   True if the ad is active.

.. code-block:: javascript

   true or false
   
.. js:data:: AdObject.datetime
   
   When the ad was published (UTC)
   
.. js:data:: AdObject.coords
   
   Coordinates.  
   
.. code-block:: javascript

   [int, int]

.. js:data:: AdObject.region

   Region based on coords.  

.. code-block:: javascript

   ["countrycode", "region", "city"]

.. js:data:: AdObject.media

   Images
   
   * Square
   * small
   * normal
   * original

.. code-block:: javascript

   [["url", "url", "url", "url"]["url", "url", "url", "url"]]

.. js:data:: UserObject.settings

   Misc keystore.

Other Objects
=============

ErrorObject
-----------

.. js:class:: ErrorObject()

   Generic Error message

.. js:data:: ErrorObject.message
   
   The error message in utf-8

.. js:data:: ErrorObject.code

   Error code.
