Classified ad's
---------------

Post a ad
~~~~~~~~~

.. http:post:: /ads

   Posts a new classified ad.

   :mimetype:`application/json`

   :form image: base64 encoded image in JPEG
   :form header: Header for the ad.
   :type header: str
   :form body: Text for the ad.
   :type body: str
   :form token: The authentication hash.
   :type token: str
   :status 200: Classified ad created successfully.
   :status 400: when form parameters are missing.
   :status 403: Authentication didn't pass

Get a list of ads
~~~~~~~~~~~~~~~~~

.. http:get:: /ads

   Get a list of ads based on filters.

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
          "ad_id": 12345,
          "author_id": "supercoolusername",
          "active": true,
          "header": "Small shed",
          "image_small": "http://akamai.cashk.am/images/fsdfd98fdas_s.jpg",
          "image": "http://akamai.cashk.am/images/fsdfd98fdas.jpg"
        },
        {
          "ad_id": 12346,
          "author_id": "supercoolusername",
          "active": true,
          "header": null,
          "image_small": "http://akamai.cashk.am/images/fsdfd99fdas_s.jpg",
          "image": "http://akamai.cashk.am/images/fsdfd99fdas.jpg"
        }
      ]

   :query offset: offset number. default is 0.
   :query limit: limit number. default is 10.
   :query username: Username of the author.
   :query region: Name of a geographical region.
   :query coordinates: Coordinates, used together with coordinates-offset.
   :query coordinates-offset: Filters out ads based on `coordinates` and the offset.
   :query text-header: Search the ad-headers for a pattern.
   :query text-all: Search the ad-headers and the ad-textbodies for a pattern.
   :statuscode 200: Success!
   :statuscode 404: No ads found.
   :statuscode 400: when dependent queries are missing.

Get all details of an ad
~~~~~~~~~~~~~~~~~~~~~~~~

.. http:get:: /ad/(int:ad_id)

   Get all the details from a `ad_id`.
   
   TODO
