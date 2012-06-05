Main Objects
============

`JSON`-notated objects returned by some of the API methods.

UserObject
----------

:http:get:`/user/(str:userId)`, :http:put:`/user/(str:userId)`, :http:get:`/users`

.. js:data:: UserObject.userId
   
   The `userId`.

.. js:data:: UserObject.userName

   The Username in utf-8.

.. js:data:: UserObject.subscription

   Status for subscription service.

TODO

AdObject
--------

:http:get:`/ads`, :http:get:`/ad/(str:adId)`, :http:put:`/ad/(str:adId)`

.. js:data:: AdObject.adId
   
   The `adId`.

TODO

Other Objects
=============

TODO
