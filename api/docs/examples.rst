Examples
========

Examples on how to consume the API.

Appcelerator
------------

`Titanium Appcelerator <http://docs.appcelerator.com/titanium/2.0/index.html>`_

Authentication
~~~~~~~~~~~~~~

A very simple and to the point example on how to retrieve a authentication token with Appcelerator.

.. https://wiki.appcelerator.org/display/guides/Handling+Remote+Data+with+HTTPClient+and+JSON

.. code-block:: javascript

    var base = "https://api.cashkamera.massforstroel.se";
    var params = "/auth?username=appuser&password=mysecretpass";
    var url = base + params;
    var xhr = Ti.Network.createHTTPClient({
        onload: function(e) {
            Ti.API.debug(this.responseText);
            json = JSON.parse(this.responseText);
            alert(json["token"]);
        },
        onerror: function(e) {
            Ti.API.debug(e.error);
            alert('error');
        },
        timeout:5000
    });
     
    xhr.open("GET", url);
    xhr.send();

