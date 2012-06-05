Authentication
--------------

Authentication should be done at the first time of use. The returned token should then be stored locally on the device and sent in every http-requests header as:

   .. sourcecode:: http
   
      GET /auth?username=colluser&password=mySecretPass412 HTTP/1.1
      Token: adsdasdljn45345+kmfsd435l%km

.. warning:: This part of the API should be considered as interim. We will probably move towards a more sustainable solution and go with OAuth2.

Authenticate app credentials
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. http:get:: /auth

   Checks credentials and returns a `Authorization Token`.
   
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
          "token": "adsdasdljn45345+kmfsd435l%km"
        }


   :query username: The username.
   :type username: str
   :query password: The password.
   :type password: str
   :status 200: User Authenticated.
   :status 400: Password or username is missing.
   :status 401: Authentication failed
   :returns: `Authorization Token`

Create app credentials
~~~~~~~~~~~~~~~~~~~~~~

.. http:post:: /auth

   Create a new login.

   :form username: The username.
   :type username: str
   :form password: The password.
   :type password: str
   :status 200: User Created successfully.
   :status 400: Password or username is missing.
   :status 409: Username already in use.
   :returns: `Authorization Token`

Modify app credentials
~~~~~~~~~~~~~~~~~~~~~~

.. http:put:: /auth/(str:username)

   :query password: The old password.
   :type password: str
   :query newPassword: The new password.
   :type newPassword: str
   :statuscode 403: User is not permitted to change credentials.
   :statuscode 404: `username` not found.
   :statuscode 401: Not logged in.
   :status 200: Success!
   
Revoke app credentials
~~~~~~~~~~~~~~~~~~~~~~

See :http:delete:`/user/(str:name)`

