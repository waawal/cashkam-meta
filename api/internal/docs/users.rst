=====
Users
=====

Users can be created based on several origins. The authentication part is therefore to be found in the :http:get:`/auth` method. All details and information however lives in the user object.

Find users
----------

.. http:get:: /users

   Returns a sequence of :js:class:`User` based on filters.

   :query name: The Username.
   :query email: The email address.
   :query country: Users country
   :query city: Users city.
   :statuscode 404: No users found.
   :statuscode 200: Success!
   :returns: A sequence of :js:class:`User`

Create a new user and user details
----------------------------------

.. http:post:: /users
   
   :form name: The Username.
   :form email: email address of the user.
   :statuscode 200: Success!
   :status 409: Username already in use.

Get user details
~~~~~~~~~~~~~~~~

.. http:get:: /users/(str:name)

   Returns a :js:class:`User`.
   
   :query name: The Username.
   :statuscode 404: :js:data:`User.name` not found.
   :statuscode 200: Success!
   :statuscode 401: Not logged in.
   :returns: :js:class:`User`

Modify user details
-------------------

E-mail address
~~~~~~~~~~~~~~

.. http:put:: /users/(str:name)

   :query name: The Username.
   :form email: email address of the user.
   :statuscode 403: User is not permitted to change details.
   :statuscode 401: Not logged in.
   :statuscode 404: :js:data:`User.name` not found.
   :statuscode 200: Success!

Remove a user
-------------

.. http:delete:: /users/(str:name)
   
   :query name: The Username.
   :statuscode 403: User is not permitted to do that (for some reason...).
   :statuscode 401: Not logged in.
   :statuscode 404: :js:data:`User.name` not found.
   :statuscode 200: Success!
