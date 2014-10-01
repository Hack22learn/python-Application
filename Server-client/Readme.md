 
   -: Server Side :-
  _______________________________________________________________________
  OPen a TCP/IP socket on a port , listen for a message from a client,
  and send an echo reply;
  This is a simple one-shot listen/reply conversation per client, But it
  goes into an infinite loop to listen for more client as long as this 
  server scripts runs;
  the client may run on a remote machine, or on same computer if it uses 
  'localhost' for server.
  
  ____________________-----------------------------_______________________
  -: Client Side :-
  ________________________________________________________________________
  Client side: use socket to send data to the server, and print server's
  reply to each message line; 
  'localhost' means that the server is running on the same machine as 
  the client, which lets us test client and server on one machine;
  to test over the internet , run a server on a remote machine;
  and set serverHost or argv[1] to machine's domain name or IP addr;
  Python sockets are portable BSD socket interface, with object methods
  for the standard socket calls available in the system's C library ..
  
  __________________---------------------------____________________________