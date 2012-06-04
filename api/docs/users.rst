Users
-----

Users can be created based on several origins. The authentication part is therefore to be found in the :http:get:`/auth` method. All details and information however lives in the user object.

Find users
~~~~~~~~~~

.. http:get:: /users

   Returns a array of `userObject` s based on filters.

   :statuscode 401: Not logged in.
   :statuscode 404: No users found.
   :statuscode 200: Success!

Create new user
~~~~~~~~~~~~~~~

.. http:post:: /users

Get user details
~~~~~~~~~~~~~~~~

.. http:get:: /user/(str:user_id)

   Returns a `userObject`.
   
   :statuscode 401: Not logged in.
   :statuscode 404: `user_id` not found.
   :statuscode 200: Success!

Change user details
~~~~~~~~~~~~~~~~~~~

.. http:put:: /user/(str:user_id)
   
   :statuscode 403: User is not permitted to change details.
   :statuscode 401: Not logged in.
   :statuscode 404: `user_id` not found.
   :statuscode 200: Success!

Remove a user
~~~~~~~~~~~~~

.. http:delete:: /user/(str:user_id)
   
   :statuscode 403: User is not permitted to do that (for some reason...).
   :statuscode 401: Not logged in.
   :statuscode 404: `user_id` not found.
   :statuscode 200: Success!
