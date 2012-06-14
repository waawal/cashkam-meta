Users
-----

Users can be created based on several origins. The authentication part is therefore to be found in the :http:get:`/auth` method. All details and information however lives in the user object.

Find users
~~~~~~~~~~

.. http:get:: /users

   Returns a sequence of :js:class:`User` based on filters.

   :query name: The Username.
   :query email: The email address.
   :query country: Users country
   :query city: Users city.
   :statuscode 404: No users found.
   :statuscode 200: Success!
   :returns: A sequence of :js:class:`User`

Create a new user
~~~~~~~~~~~~~~~~~

.. http:post:: /users
   
   :form name: The Username.
   :form contact.address: Address.
   :form contact.phone: Phone number.
   :form contact.postalcode: Postal code.
   :form contact.country: Country.
   :form contact.city: City.
   :form contact.name: The real name of the user.
   :form email: email address of the user.
   :statuscode 200: Success!
   :status 409: Username already in use.

.. http:post:: /user/(str:name)/contact

   :query name: The Username.
   :form address: Address.
   :form phone: Phone number.
   :form postalcode: Postal code.
   :form country: Country.
   :form city: City.
   :statuscode 403: User is not permitted to change details.
   :statuscode 401: Not logged in.
   :statuscode 404: :js:data:`User.name` not found.
   :statuscode 200: Success!

.. http:post:: /user/(str:name)/storage

   :query name: The Username.
   :form key: Can be any string, sets the key to the submitted value.
   :statuscode 403: User is not permitted to change details.
   :statuscode 401: Not logged in.
   :statuscode 404: :js:data:`User.name` not found.
   :statuscode 200: Success!

Get user details
~~~~~~~~~~~~~~~~

.. http:get:: /user/(str:name)

   Returns a :js:class:`User`.
   
   :query name: The Username.
   :statuscode 404: :js:data:`User.name` not found.
   :statuscode 200: Success!
   :statuscode 401: Not logged in.
   :returns: :js:class:`User`

Modify user details
~~~~~~~~~~~~~~~~~~~

.. http:put:: /user/(str:name)

   :query name: The Username.
   :form email: email address of the user.
   :statuscode 403: User is not permitted to change details.
   :statuscode 401: Not logged in.
   :statuscode 404: :js:data:`User.name` not found.
   :statuscode 200: Success!

.. http:put:: /user/(str:name)/contact

   :query name: The Username.
   :form address: Address.
   :form phone: Phone number.
   :form postalcode: Postal code.
   :form country: Country.
   :form city: City.
   :statuscode 403: User is not permitted to change details.
   :statuscode 401: Not logged in.
   :statuscode 404: :js:data:`User.name` not found.
   :statuscode 200: Success!

.. http:put:: /user/(str:name)/storage

   :query name: The Username.
   :form key: Can be any string, sets the key to the submitted value.
   :statuscode 403: User is not permitted to change details.
   :statuscode 401: Not logged in.
   :statuscode 404: :js:data:`User.name` not found.
   :statuscode 200: Success!

Remove a user
~~~~~~~~~~~~~

.. http:delete:: /user/(str:name)
   
   :query name: The Username.
   :statuscode 403: User is not permitted to do that (for some reason...).
   :statuscode 401: Not logged in.
   :statuscode 404: :js:data:`User.name` not found.
   :statuscode 200: Success!
