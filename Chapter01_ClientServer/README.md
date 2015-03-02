# Server and Client

### gopherClient.py & gopherClient2.py & gopherClient3.py

	$ python gopherClient.py quux.org /
	$ python gopherClient2.py quux.org /
	$ python gopherClient3.py quux.org /

And just check the result.

### server.py

	$ python server.py

Then open another terminal and:
	
	$ telnet localhost 10086

### gopherClient.py

Not so useful now.

### download.py

	$ python download.py http://www.baidu.com > baiduHomepage.html