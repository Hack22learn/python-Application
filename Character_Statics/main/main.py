# Python 2.7.6
#  -___-Main-___-
# To calculate % use of each alphabet in any text document

#import anydbm 
from hist import *
from store import *


def option():
    print '1 : New input File \n 2 : clear data \n 3: Exit program '
    op = int(raw_input('Enter your option : '))

    alpha ='abcdefghijklmnopqrstuvwxyz' # these are char which % occurence we have to calculate
    
    if op == 1:
        print 'Put your text file in current folder then '
        filename = str(raw_input('Enter file name with extention : '))
        hs=hist(filename) #create object of class hist
        hs.histogram() #itterate operation on file for calculation of accurence
        print 'result of this itteration is :'
        ## print result of this itteration in regular order a ...z
        for key in alpha:
            if key in hs.data:
                print key,'  =>  ',hs.data[key]
            else:
                print key,'  =>  ',0

        #overal result 
        db = database() #create object of class database
        database.add_store(db,hs.data) # update database
        db.result() #update result.txt file
        db.close_db() #close database connect
        print '\n\n'
        option()
        
    elif op == 2:
        db=database() #create object of class database
        db.refresh_database() #  Reset database to 0
        print 'database refresed \n\n'
       # print db.Data  ##To check data is refresed or not
        option()

    elif op == 3:
        print " thank uu.... "
        exit()
        
if __name__=='__main__':
  print "Welcome to histogram\n"
  option()
