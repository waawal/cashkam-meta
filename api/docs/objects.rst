Main Objects
============

`JSON`-notated objects returned by some of the API methods.

UserObject
----------

:http:get:`/user/(str:userId)`, :http:get:`/users`

.. js:class:: UserObject

   A object representing a user.

.. js:data:: UserObject.userId
   
   The `userId`.

.. js:data:: UserObject.userName

   The Username in utf-8.

.. js:data:: UserObject.subscription

   Status for subscription service.

TODO

AdObject
--------

:http:get:`/ads`, :http:get:`/ad/(str:adId)`

.. js:class:: AdObject

   A object representing a ad.

.. js:data:: AdObject.adId
   
   The `adId`.

TODO

Other Objects
=============

ErrorObject
-----------

.. js:class:: ErrorObject()

   Generic Error message

.. js:data:: ErrorObject.message
   
   The error message in utf-8
