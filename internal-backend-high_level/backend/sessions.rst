Sessions
========

Sessions are stored in ``Redis`` hashes. There is a difference between App= and Web=session due to our current dual approach for pushing of data.

  Websessions
Web sessions identifies theirselves by sending their auth=info in a cookie.

  Appsessions
App=sessions as opposed to the web=sessions sends their auth credentials in the HTTP=header.

Streaming
---------

Streaming of data to sessions is achieved by the implementation of two technologies. On the app=side we use secure ``websockets`` and in the webbrowser we use ``ServerEvents`` since we don't need duplexed communication.
