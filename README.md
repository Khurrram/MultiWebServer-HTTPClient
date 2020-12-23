# MultiWebServer-HTTPClient
Features a multithreaded server and a client. Once the server is run, it is hosted off of 127.0.0.1:1500. If you have an html file in the same directory, you can access the the file through the browser by typing in the url [ 127.0.0.1:1500/file.html ]. The file can also be reached through terminal, in which case you would have to run the client.py file. This would display the contents of the file in the terminal.
------------
Multi-Threaded Server
File Name : mtserver.py
Instructions : You can just double-click in order to run the server, which in default is hosted on 127.0.0.1:1500. If you want to run through terminal, the command format is [ py mtserver.py ] while you are in this directory.
------------
Client
File Name : client.py
Instructions : You need to run this client through terminal. The command format is [ client.py server_host server_port filename ] . 
If you would like to see the print statements, the command format is [ py client.py server_host server_port filename ] .
-------------

In order to run these two in conjunction, first start the Multi-Threaded Server, and then run the client with command [ py client.py 127.0.0.1 1500 (filename) ]
This will attempt to fetch this file from the server's directory.
