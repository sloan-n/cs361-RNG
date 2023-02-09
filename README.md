# cs361-RNG
Random Number Generator Microservice

This program is a microservice that sends a randomly generated integer between 1 and 100 through a TCP socket.

Communication Contract

1. Requesting data:
The server will be binded to port 5500 and listen for up to 5 connections at a time. The server recieves a request through a client connection using .accept(). The client will connect using .connect(). The client does NOT need to send a message, the connection is the request. Once the connection is made, the server will call the random number generator function to generate a random integer. The server will then send the random integer to the client using .send() and close the connection with the client.

2. Recieving data
To recieve the message from the server after connecting to the server, the client will need to use .recv() to get the data from the server. The message will need to be use .decode() to convert the bytes to a string. The recieved data is the randomly generated integer as a string. NOTE: If you would like to use the randomly generated number as an integer, remember to convert it to an integer first.

3. UML Sequence Diagram
![UML - RNG](https://user-images.githubusercontent.com/81350636/217755306-e3d04d67-ee13-4fb8-956d-589172f63e60.jpg)

