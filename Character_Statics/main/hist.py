# Histogram hist class def

import string

class hist(object):
    '''
        This class define all neccessary function to calculate histogram of given data
    '''
    def __init__(self,filename=''): #define initiate method
        self.Fname = filename
        self.data=dict()

    def __str__(self): #define __str__ method control way to print class hist object
        return 'Input file name = %s \n %s ' %(self.Fname, self.data)
                                              

    def histogram(self):
        """
            This functon is basically an itterator it itterate txt file and calculate accurence of each charactor
        """
        try: # exception handler
            fin =open(self.Fname) #open file
        except:
                print 'Input file',self.Fname,' Not found'
                
        for line in fin: # select single line at a time
            for word in line:
                word = word.strip(string.punctuation + string.whitespace)  #remove punctuation & white space
                word = word.lower() #convert to lower case letters
                for ch in word:
                    if ch not in self.data: # if ch is not in data dict then add new entry
                        self.data[ch] =1
                    else:    #increment value of entry
                        self.data[ch] +=1
        

#------------------------------------------------------------------------------------
if __name__=='__main__':
    print 'http://beginer2cs.blogspot.com'
