__author__ = 'Sudhanshu Patel'

import urllib2
import os

class EHarvestor():
    def __init__(self,url,fname):
        self.url=url
        self.data=''
        self.file=fname
        self.counter=0

    def get_data(self):
        # Get data from web
        '''
         connect to given url and store data of that page in a variable
         then return that var
        '''
        try:
            print 'Try TO connect To server'
            response=urllib2.urlopen(self.url)
            print 'found responce :)'
            print 'Try to fetch all data from url for further processing'
            self.data=response.read()
            print "Data Copied, "
            return True
        except:
            return False

    def extractMail(self):
        '''
            Extract mail & write It to file
        '''
        try:
            if not os.path.exists('Extracted_Data'):
                os.makedirs('Extracted_Data')
            f=open(self.file,'w')
        except:
            print('Unable to create directory or file:',self.file)
            print('exiting ......... :(')
            exit()
        while True:
            strt=self.data.find("(at)")
            if strt !=-1:
                sub=self.data[strt-60:strt+50]
                beg=sub.find('<td>')
                end=sub.find('</td>',60)
                if beg !=-1 and end !=-1:
                    stt=sub[beg+4:end-4]
                    f.write(stt+'\n')
                    self.data=self.data[strt+20:]
                    self.counter+=1 #increment count
                    if self.counter %100==0:
                        print("Email Extracted Count : ",self.counter)
                else:
                    self.data=self.data[strt+20:]
            else:
                f.write('TOTAL Email Harvested : '+str(self.counter))
                break
        f.close()






