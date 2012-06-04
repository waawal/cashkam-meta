Authentication
--------------

Authentication is provided a little differently in the internal API as opposed to the planned public. The public is based on basic-auth.

**Warning** This part of the API should be considered as a interim. We will probably move to a more sustainable solution and go with OAuth2.

Validate a application user
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. http:post:: /auth

   Checks credentials and returns a authentication token. This method will not be available in the public API.
   
   It accepts :http:method:`post` only.

   :mimetype:`application/json`
   
   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: application/json

        {
          "token": "adsdasdljn45345+kmfsd435l%km"
        }



   :form username: The username.
   :type username: str
   :form password: The password.
   :type password: str
   :status 200: User Authenticated.
   :status 400: Password or username is missing.
   :status 401: Authentication failed

Create a application user based on external authentication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. http:post:: /auth

TODO
