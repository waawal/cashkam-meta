Classified Ad's
---------------

Get a list of ads
~~~~~~~~~~~~~~~~~

.. http:get:: /ads

   Get a list of ads based on filters. Returns a sequence (array) of :js:class:`Ad` s.

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
          "_id": fsdfg342fds,
          "user": "supercoolusername",
          "active": true,
          "text": "Small shed.\n Cute!",
          "title": "Small shed",
          "media": [["http://akamai.cashk.am/images/fsdfd98fdas_square.jpg", http://akamai.cashk.am/images/fsdfd98fdas_s.jpg, http://akamai.cashk.am/images/fsdfd98fdas_m.jpg, http://akamai.cashk.am/images/fsdfd98fdas.jpg]],
          "timestamp": 1338882525,
          "coords": [51.500611, 0.124611],
          "region": ["uk", "london", "london"]
        },
        {
          "_id": fsdfg242fds,
          "user": "supercoolusername",
          "active": true,
          "text": null,
          "title": null,
          "media": [["http://akamai.cashk.am/images/fsdfd98fdas_square.jpg", http://akamai.cashk.am/images/fsdfd98fdas_s.jpg, http://akamai.cashk.am/images/fsdfd98fdas_m.jpg, http://akamai.cashk.am/images/fsdfd98fdas.jpg]],
          "timestamp": 1338882525,
          "coords": [51.500611, 0.124611],
          "region": ["uk", "london", "london"]
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
   :returns: `sequence` of :js:class:`Ad`

Publish a ad
~~~~~~~~~~~~

.. http:post:: /ads

   Posts a new classified ad.

   :mimetype:`application/json`

   :form image: base64 encoded image in JPEG
   :form text: Text for the ad.
   :form coords: The coordinates.
   :status 200: Classified ad created successfully.
   :status 400: when form parameters are missing.
   :statuscode 403: User is not permitted to create a ad.
   :statuscode 401: Not logged in.
   :returns: :js:data:`Ad._id`

Get ad details
~~~~~~~~~~~~~~

.. http:get:: /ad/(str:_id)

   Get all the details from a :js:data:`Ad._id`.
   
   :statuscode 404: :js:data:`Ad._id` not found.
   :statuscode 200: Success!
   :returns: :js:class:`Ad`

Modify a ad
~~~~~~~~~~~

.. http:put:: /ad/(str:_id)
   
   Changes/adds to a already published ad.

   :query image: base64 encoded image in JPEG
   :query text: Text for the ad.
   :query coords: The coordinates.
   :statuscode 403: User is not permitted to modify the ad
   :statuscode 401: Not logged in.
   :statuscode 404: :js:data:`Ad._id` not found.
   :statuscode 200: Success!

Remove a ad
~~~~~~~~~~~

.. http:delete:: /ad/(str:_id)
   
   Deactivates a ad. Ads are never removed/deleted per se.
   
   :statuscode 200: Success, Ad deactivated.
   :statuscode 404: :js:data:`Ad._id` not found.
   :statuscode 403: User is not permitted to modify the ad.
   :statuscode 401: Not logged in.
