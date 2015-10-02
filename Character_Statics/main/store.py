# Python 2.7.6
# Data store & retrive

import anydbm #for python anydbm database
                               #histo.db is file where this program store its data work

# important : anydb store data as string always
class  database(object):
    '''
       This class is used for data updation , storation & retrive from basic database
       anydbm
    '''
    def __init__(self):
        self.Data=anydbm.open('histo.db','c') # here 'c' stan for if histo.db not availabe create it
        # open database histo.db
    def __str__(self):
        for key in self.Data:
            print key,' => ',self.Data[key]

    def add_store(self,dic): #operator overloading for addition
        '''
          (object of type database , dictionary) => store addtion in database
          { Update database}
        '''
        if isinstance(dic,database):
            print 'second argument must be a dictionary'
        else:
            for key in dic:
                if(key in self.Data):
                    self.Data[key] = str(int(self.Data[key])+dic[key])
                else:
                    self.Data[key]=str(dic[key])
    def close_db(self):
        '''
        close database connection
       '''
        self.Data.close()

    def result(self):
        '''
        calculate result & print & copy it to result.txt
        it gives overall result average of all calculation till now
       '''
        total=0.0
        for key in self.Data:
            total +=float(self.Data[key])

        fout = open('result.txt','w')
        fout.write('Note : this is overall result from all data this program encounter  till now\n\n ')
        fout.write('    char        =>     %age\n')
        
        for key in 'abcdefghijklmnopqrstuvwxyz':
            if key in self.Data:
                fout.write('\n      '+key+'               '+str((float(self.Data[key])/total)*100)+' %'+'\n     -------------------------')
            else:
                fout.write('\n      '+key+'               '+str(0)+' %'+'\n     -------------------------')

        print 'Output of % use of alphabets is store to "output.txt"  in current directory'

        fout.close() # close result file

    def refresh_database(self):
        """
         Reset database to 0
        """
        for key in self.Data:
            self.Data[key] = str(0)

        fout = open('result.txt','w')  #open output folder & reset to Null
        fout.write('All Data is Reset \n  Thanks \n Sudhanshu Patel  => sudhanshuptl13@gmail.com')
        fout.close() #close output folder

#---------------------------------------------------------------------
if __name__=='__main__':
    print 'http://beginer2cs.blogspot.com'
            
        
