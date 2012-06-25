========
Contacts
========

Create Contact
--------------

.. http:post:: /contacts/(str:name)

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

Modify Contact
--------------

.. http:put:: /contacts/(str:name)

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

Get Contact details
-------------------

.. http:get:: /contacts/(str:name)

   :query name: The Username.
   
   :query address: Address.
   :query phone: Phone number.
   :query postalcode: Postal code.
   :query country: Country.
   :query city: City.
   :statuscode 403: User is not permitted to retrieve contact details.
   :statuscode 401: Not logged in.
   :statuscode 404: :js:data:`User.name` not found.
   :statuscode 200: Success!

Get Contact address
~~~~~~~~~~~~~~~~~~~

.. http:get:: /contacts/(str:name)/address

   :query name: The Username.
   
   :statuscode 403: User is not permitted to retrieve contact details.
   :statuscode 401: Not logged in.
   :statuscode 404: :js:data:`User.name` not found.
   :statuscode 200: Success!
   
Get Contact phone number
~~~~~~~~~~~~~~~~~~~~~~~~

.. http:get:: /contacts/(str:name)/phone

   :query name: The Username.
   
   :statuscode 403: User is not permitted to retrieve contact details.
   :statuscode 401: Not logged in.
   :statuscode 404: :js:data:`User.name` not found.
   :statuscode 200: Success!
   
Get Contact postal code/ ZIP-code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. http:get:: /contacts/(str:name)/postalcode

   :query name: The Username.
   
   :statuscode 403: User is not permitted to retrieve contact details.
   :statuscode 401: Not logged in.
   :statuscode 404: :js:data:`User.name` not found.
   :statuscode 200: Success!

Get Contact country
~~~~~~~~~~~~~~~~~~~

.. http:get:: /contacts/(str:name)/country

   :query name: The Username.

   :statuscode 403: User is not permitted to retrieve contact details.
   :statuscode 401: Not logged in.
   :statuscode 404: :js:data:`User.name` not found.
   :statuscode 200: Success!
   
Get Contact city
~~~~~~~~~~~~~~~~~~~

.. http:get:: /contacts/(str:name)/city

   :query name: The Username.
   
   :statuscode 403: User is not permitted to retrieve contact details.
   :statuscode 401: Not logged in.
   :statuscode 404: :js:data:`User.name` not found.
   :statuscode 200: Success!

Remove a contact
----------------

.. http:delete:: /contacts/(str:name)
   
   :query name: The Username.
   :statuscode 403: User is not permitted to do that.
   :statuscode 401: Not logged in.
   :statuscode 404: :js:data:`User.name` not found.
   :statuscode 200: Success!
