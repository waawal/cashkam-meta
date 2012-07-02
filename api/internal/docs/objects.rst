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
   
.. js:data:: User.email

   Email-address.  

.. js:data:: User.contacts

   Reference to :js:data:`Contact._id` associated with the user.

.. js:data:: User.timestamp
   
   timedate when user was created (UTC)

.. js:data:: User.storage

   Misc keystore.

Contact Object
--------------

.. js:class:: Contact

   A object representing a user's contact information.

.. js:data:: Contact._id
   
   The id of the Contact.

.. js:data:: Contact.username

   :js:data:`User.name` associated with this contact.

.. js:data:: Contact.address

   Address details for user.  

.. js:data:: Contact.city

   City name of the user.  
   
.. js:data:: Contact.phone

   Phone number in international format (without the + char).  

.. js:data:: Contact.postalcode

   Postal code/zip-code of the user.  

.. js:data:: Contact.realname

   The real name of the user.  
   
.. js:data:: Contact.country

   Country of the user.

Ad Object
---------

:http:get:`/ads`, :http:get:`/ad/(str:_id)`

.. js:class:: Ad

   A object representing a ad.

.. js:data:: Ad._id
   
   The id of the ad.

.. js:data:: Ad.user
   
   Published by :js:data:`User.name`

.. js:data:: Ad.biddable
   
   true if the ad is set to auction status.

.. js:data:: Ad.expires
   
   When the ad should expire or (end of auction in case biddable is true) (UTC)

.. code-block:: javascript

   true or false

.. js:data:: Ad.text
   
   The ad text.

.. js:data:: Ad.title
   
   The title of the ad.
   
.. js:data:: Ad.active
   
   True if the ad is active.

.. code-block:: javascript

   true or false
   
.. js:data:: Ad.timestamp
   
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

   Reference to :js:class:`Media` of the ad.

.. js:data:: Ad.storage

   Misc keystore.

Media Object
------------

.. js:class:: Media

   A object representing the media associated with a ad.

.. js:data:: Media._id
   
   The id of the Media.

.. js:data:: Media.ad

   Associated with :js:data:`Ad._id`

.. js:data:: Media.images

   All images except the main image.
   
   * square
   * small
   * normal
   * original

.. code-block:: javascript

   [["url", "url", "url", "url"]["url", "url", "url", "url"]]

.. js:data:: Media.main
   
   The image representing the ad in search-results etc.
   
.. code-block:: javascript

   * square
   * small
   * normal
   * original

.. code-block:: javascript

   ["url", "url", "url", "url"]

   

Response Objects
================

Error Object
------------

.. js:class:: Error()

   Generic Error message

.. js:data:: Error.message
   
   The error message in utf-8

.. js:data:: Error.code

   Error code.

Response Object
---------------

.. js:class:: Response()

   Generic Response

.. js:data:: Response.response
   
   Response to be parsed as JSON

