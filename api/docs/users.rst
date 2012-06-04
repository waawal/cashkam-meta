Users
-----

Users can be created based on several origins. The authentication part is therefore to be found in the :http:get:`/auth` method. All details and information however lives in the user object.

Find users
~~~~~~~~~~

.. http:get:: /users

   Returns a array of `userObject`s based on filters.

Create new user
~~~~~~~~~~~~~~~

.. http:post:: /users

Get user details
~~~~~~~~~~~~~~~~

.. http:get:: /user/(str:user_id)

   Returns a `userObject`.

Change user details
~~~~~~~~~~~~~~~~~~~

.. http:put:: /user/(str:user_id)

Remove a user
~~~~~~~~~~~~~

.. http:delete:: /user/(str:user_id)
