Authentication
--------------

Authentication is provided a little differently in the internal API as opposed to the planned public. The public is based on basic-auth.

.. warning:: This part of the API should be considered as interim. We will probably move towards a more sustainable solution and go with OAuth2.

Authenticate app credentials
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. http:get:: /auth

   Checks credentials and returns a `authToken`.
   
   It accepts :http:method:`get` only.

   :mimetype:`application/json`
   
   **Example request**:

   .. sourcecode:: http

      GET /auth?username=colluser&password=mySecretPass412 HTTP/1.1
      Host: cashk.am
      Accept: application/json, text/javascript
   
   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: application/json

        {
          "authToken": "adsdasdljn45345+kmfsd435l%km"
        }



   :query username: The username.
   :type username: str
   :query password: The password.
   :type password: str
   :status 200: User Authenticated.
   :status 400: Password or username is missing.
   :status 401: Authentication failed

Create app credentials
~~~~~~~~~~~~~~~~~~~~~~

.. http:post:: /auth

   Returns a `authToken`.

   :form username: The username.
   :type username: str
   :form password: The password.
   :type password: str
   :status 200: User Created successfully.
   :status 400: Password or username is missing.
   :status 409: Username already in use.

Change app credentials
~~~~~~~~~~~~~~~~~~~~~~

.. http:put:: /auth/(str:userId)

   :query old_password: The old password.
   :type old_password: str
   :query new_password: The new password.
   :type new_password: str
   :statuscode 403: User is not permitted to change credentials.
   :statuscode 404: `userId` not found.
   :statuscode 401: Not logged in.
   
