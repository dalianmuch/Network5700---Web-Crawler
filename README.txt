High-Level Approach
1st use a socket to send a GET request to the server page to get the csrftoken and sessionid.
2nd use another socket to send a POST request to the server with username password and csrftoken to login,
receive another sessionid, save this new sessionid into the cookie and all the next GET requests should bring this
cookie into the header
3rd use another socket to send a GET request to the home page, retrieve friends' fakebook links
4th do BFS algorithm for each page, use new socket for each http request


Challenges You Faced
1st:
I cannot login when sending the form data, I fixed the problem by setting the "Content-Length" in request header.
2nd:
I find the socket connection too slow. The server will reply the response to me only
when the 5 seconds keep-alive waiting time expires.
Therefore, I change all requests with header "Connection: close".
In that way, my requests can get immediate responses and my web crawler can finish in 3 minutes.
3rd:
The socket cannot do a second job. I fixed this by letting every http request sent by a new socket.

##### Server Time Out #####
There are some times the socket cannot connect to the server,
it will return "socket.error: [Errno 60] Operation timed out" with the code "s.connect((host, port))"
I fixed this problem by using try: except:. If this error is arised, I will continue to try with another socket to connect.
It may take like 60 seconds to wait until the error is arised and be thrown, but the code works eventually.


Overview of How You Tested Your Code
1st. Tried different arguments on command lines
2nd. Handle error status code
