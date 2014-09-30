from socket import *
myHost=''  # '' = All Available interface on Host
myPort=5007 # listen on a Non -Reserve port

sockobj=socket(AF_INET,SOCK_STREAM) #make TCP Socket object
sockobj.bind((myHost,myPort)) #Bind it to server port Address
sockobj.listen(3) #Listen Allow 3 pending Connects

while True:
    connection,address=sockobj.accept() #Wait for Next Client Connect
    print 'server connected by ',address
    while True:
        data=connection.recv(1024)
        if not data :
            break
        connection.send(b'Echo>> '+ data)
    connection.close()

raw_input('END')
