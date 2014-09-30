import sys
from socket import *
serverHost='localhost' #server name or domain name
serverPort=5007 #none reserved port used by server
message=[b'hello server ,' , b'I am Sudhanshu Patel ,', b'I just Wanna check How GOOD you are ', b' thanks Bye!!'] #default text send to server
if len(sys.argv)>1:
    serverHost=sys.argv[1]   #server address provided by user
    if len(sys.argv)>2:
        message=(x.encode() for x in sys.argv[2:])  #Message to send provided by user

sockobj=socket(AF_INET,SOCK_STREAM) #make TCP/Ip socket object
try:
    sockobj.connect((serverHost,serverPort)) #Connect to server machine on given port
except:
    print "'Can't Connect'"

for line in message:
    sockobj.send(line)  #send one line to server over socket
    data=sockobj.recv(1024) #recive responce from server upto 1k
    print 'Client recv >>',data
sockobj.close()
raw_input('END')

