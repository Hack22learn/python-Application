import socket
import sys

class HubScanner():
    def __init__(self,port=411):
        self.port=411

    def scan_classB_network(self,subnet):
        # Scan All IP for open connection at port 411 in that subnet
        subnet=str(subnet)
        active_hub=[]
        count=0
        try:
            for i in range(192,233):
                for j in range(256):
                    serverIP=subnet+'.'+str(i)+'.'+str(j)
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(0.1)
                    result = sock.connect_ex((serverIP, self.port))
                    if result== 0:
                        active_hub.append(serverIP)
                        print 'Active DC ServerIP >> >>',serverIP
                    sock.close()
                    count +=1
                    if count %50==0:
                        print  count,'Ip Scanned -----------------------'
            return active_hub
        except KeyboardInterrupt:
            print "You pressed Ctrl+C"
            sys.exit()

        except socket.gaierror:
            print 'Hostname could not be resolved. Exiting'
            sys.exit()
        except socket.error:
            print "Couldn't connect to server"
            sys.exit()

def file_write(ls):
    #write content of ls to file
    f=open('Active DC HUb.txt','w')
    for line in ls:
        f.write(line+'\n')
    f.close()

if __name__=='__main__':
    subnet=raw_input('Enter ClassB subnet ex: 192.168  :>>')
    obj=HubScanner() #craete an object
    ls=obj.scan_classB_network(subnet) 
    file_write(ls)
    print 'All  Active DC Ip is saved in >> "Active DC HUb.txt"'
    raw_input('Bye ... ')
