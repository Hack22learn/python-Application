#!/usr/bin/env python
#This application used to map nitrkl all IP and i=ts user

from socket import *
import sys

class MapMyNITR(object):
    '''
           Used to mapp all nitrkl IP and its user sytem
    '''
    def __init__(self,filename='NITR_mapping.txt'):
        self.fname=filename
        try:
            self.f=open(self.fname,'w')
        except:
            print 'unable to open text file'
    
    def is_up(self,addr):
        s = socket(AF_INET, SOCK_STREAM)
        s.settimeout(0.1)    ## set a timeout of 0.01 sec
        if not s.connect_ex((addr,135)):    # connect to the remote host on port 135
            s.close()                       ## (port 135 is always open on Windows machines, AFAIK)
            return 1
        else:
            s.close()
            
    def map_nitr_run(self):
        ip_suff='192.168.'
        ip_mid=0
        ip_post=0
        count=0
        try:
            print "SrNo.\t\tIp Addres         ->      getfqdn(addr)"
            self.f.write("\t\tIp Addres         ->      getfqdn(addr)\n\n")
            for i in xrange(ip_mid,256):
                for ip in xrange(ip_post,256):    ## 'ping' addresses 192.168.1.1 to .1.255
                    addr = ip_suff +str(i)+'.'+ str(ip)
                    if self.is_up(addr):
                        count +=1
                        st=str(count)+'\t\t%s \t ->> %s \n' %(addr, getfqdn(addr)) #getfqdn(addr) returns :-fully qulified domain name for given host name                  :
                        print st
                        self.f.write("\t\t"+st)
                    
            print 'We R done check your file :- for organise result'
            self.f.close()
            
        except KeyboardInterrupt:
            print 'You Press Ctrl+c'
            sys.exit()
            
        except error:
            print "Couldn't connect to server"
            sys.exit()
        
        
if __name__=='__main__':
    print 'Should we start mapping NITR (YES/NO)'
    check=raw_input()
    if check=='YES' or check=='yes' or check=='Yes':
        obj=MapMyNITR()
        obj.map_nitr_run()
    else:
        print 'thanks'
        sys.exit()
    
                
        
        
