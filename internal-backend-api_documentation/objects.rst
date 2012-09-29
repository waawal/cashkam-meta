Main Data
=========

`JSON`-notated objects returned by some of the API methods.

..  note::
    Please note that this representation does not reflect the schemas used for the storage of this data.

User
----

:http:get:`/user/(str:name)`, :http:get:`/users`

A Collection of user data.

..  note::
    The index is the username (not _id!).

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

.. js:data:: User.timestamp
   
   timedate when user was created (UTC)

.. js:data:: User.storage

   Misc keystore.

Contact
-------

Contact details for a user.

.. js:class:: Contact

   A object representing a user's contact information.

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

Ad
--

:http:get:`/ads`, :http:get:`/ad/(str:_id)`

.. js:class:: Ad

   A object representing a ad.

.. js:data:: Ad._id
   
   The id of the ad.

.. js:data:: Ad.user
   
   Published by :js:data:`User.name`

.. js:data:: Ad.price
   
   Fixed price (or highest bid if auction).

.. js:data:: Ad.currency
   
   Currency of the price

.. js:data:: Ad.biddable
   
   true if the ad is set to auction status.

.. code-block:: javascript
   
   true or false

.. js:data:: Ad.bids

   A Array of arrays containing all bids.
   
   * Amount
   * Username
   * Timestamp (UTC)

.. code-block:: javascript

   [[60, "kollo89", 816516847], [50, "anderskarlsson", 813542448,]]

.. js:data:: Ad.expires
   
   When the ad should expire or (end of auction in case biddable is true) (UTC)

.. code-block:: javascript

   true or false

.. js:data:: Ad.text
   
   The ad text.

.. js:data:: Ad.title
   
   The title of the ad.

.. js:data:: Ad.tag
   
   The category of the ad.

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

.. js:data:: Ad.locale

   The language of the ad.

.. code-block:: javascript
   
   ["se","sv"]

.. js:data:: Ad.storage

   Misc keystore.

Media
-----

.. js:class:: Media

   A object representing the media associated with a ad.

.. js:data:: Media.images

   All images except the main image.
   
   * square
   * small
   * normal
   * original

.. code-block:: javascript

   [["url", "url", "url", "url"], ["url", "url", "url", "url"]]

.. js:data:: Media.main
   
   The image representing the ad in search-results etc.
   
   * square
   * small
   * normal
   * original

.. code-block:: javascript

   ["url", "url", "url", "url"]

Response Data
=============

Error
-----

.. js:class:: Error()

   Generic Error message

.. js:data:: Error.message
   
   The error message in utf-8

.. js:data:: Error.code

   Error code.

Response
--------

.. js:class:: Response()

   Generic Response

.. js:data:: Response.response
   
   Response to be parsed as JSON

