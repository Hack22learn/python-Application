#Python 2
__author__ = 'Sudhanshu Patel'

from  EmHarvestor import *

if __name__=='__main__':
    url='file:///D:/Sem%207/Email%20Harvesting/data%20set/14_APR_I.html'
    filename='14AprilII'
    #url=str(raw_input('Enter Url: '))
    #filename=raw_input('Enter file name to save data :')
    harvester=EHarvestor(url,filename+'.txt')
    if harvester.get_data():
        print('Harvesting Process Start :)')
        harvester.extractMail()
        print '''Thank You For Using ME :)'''
    else:
        print("Unable to fetch data from url :"+url)
        print('check Url Again :(')




