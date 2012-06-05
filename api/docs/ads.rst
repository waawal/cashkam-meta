Classified ad's
---------------

Get a list of ads
~~~~~~~~~~~~~~~~~

.. http:get:: /ads

   Get a list of ads based on filters. Returns a array of :js:class:`AdObject` s.

   **Example request**:

   .. sourcecode:: http

      GET /ads?limit=2&username=supercoolusername HTTP/1.1
      Host: cashk.am
      Accept: application/json, text/javascript

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: application/json

      [
        {
          "adId": fsdfg342fds,
          "userId": "supercoolusername",
          "active": true,
          "header": "Small shed",
          "imageSmall": "http://akamai.cashk.am/images/fsdfd98fdas_s.jpg",
          "image": "http://akamai.cashk.am/images/fsdfd98fdas.jpg"
        },
        {
          "adId": adfsg4fa834r,
          "userId": "supercoolusername",
          "active": true,
          "header": null,
          "imageSmall": "http://akamai.cashk.am/images/fsdfd99fdas_s.jpg",
          "image": "http://akamai.cashk.am/images/fsdfd99fdas.jpg"
        }
      ]

   :query offset: offset number. default is 0.
   :query limit: limit number. default is 10.
   :query username: Username of the author.
   :query region: Name of a geographical region.
   :query coordinates: Coordinates, used together with coordinates-offset.
   :query coordinates-offset: Filters out ads based on `coordinates` and the offset.
   :query text: Search the text of the ads for a pattern.
   :statuscode 200: Success!
   :statuscode 404: No ads found.
   :statuscode 400: when dependent queries are missing.

Post a ad
~~~~~~~~~

.. http:post:: /ads

   Posts a new classified ad. Returns a :js:data:`AdObject.adId`.

   :mimetype:`application/json`

   :form image: base64 encoded image in JPEG
   :form header: Header for the ad.
   :type header: str
   :form body: Text for the ad.
   :type body: str
   :form coordinates: The coordinates.
   :form token: The authentication hash.
   :type token: str
   :status 200: Classified ad created successfully.
   :status 400: when form parameters are missing.
   :statuscode 403: User is not permitted to create a ad.
   :statuscode 401: Not logged in.

Get all details of an ad
~~~~~~~~~~~~~~~~~~~~~~~~

.. http:get:: /ad/(str:adId)

   Get all the details from a :js:data:`AdObject.adId`.
   
   :statuscode 404: :js:data:`AdObject.adId` not found.
   :statuscode 200: Success!
   :returns: :js:class:`AdObject`

Change a ad
~~~~~~~~~~~

.. http:put:: /ad/(str:adId)
   
   Changes/adds to a already published ad.

   :statuscode 403: User is not permitted to modify the ad
   :statuscode 401: Not logged in.
   :statuscode 404: :js:data:`AdObject.adId` not found.
   :statuscode 200: Success!

Remove a ad
~~~~~~~~~~~

.. http:delete:: /ad/(str:adId)
   
   Deactivates a ad. Ads are never removed/deleted per se.
   
   :statuscode 200: Success, Ad deactivated.
   :statuscode 404: :js:data:`AdObject.adId` not found.
   :statuscode 403: User is not permitted to modify the ad.
   :statuscode 401: Not logged in.
