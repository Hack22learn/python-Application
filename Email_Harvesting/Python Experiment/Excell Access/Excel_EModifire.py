__author__ = 'Sudhanshu Patel'

from xlrd import open_workbook
import codecs
import sys
import time

def remove_anomaly(s):
    #Remove or replace data with ascii value greter than 128
    cell_data=''
    for ch in s:
       if ord(ch) <127:
           cell_data +=ch
    return cell_data




if __name__=='__main__':
    count=0
    f_name=raw_input('Enter Excel file name with extention :')
    try:
        wb = open_workbook(f_name) #Open File to read
        try:
            res=open('res.txt','w')
        except:
            print 'Error in opning result file'
            exit()
    except:
        print 'Error in opening Input file'
        exit()

    for s in wb.sheets(): # If More Than One Seet in Excel File , Even Then It process all data in all sheets
        print 'Sheet:',s.name
    for row in range(1,s.nrows): #for data in each row except the first row, as it is title of each row
        #values = []
        Error=False
        for col in range(s.ncols): #for data in in row=rowX and coloumn=col
            if col==1:
                try:
                    cell_data=str(s.cell(row,col).value)
                    values=cell_data.replace('>','')
                except:
                    try:
                        values=remove_anomaly(s.cell(row,col).value)
                    except:
                        print 'Error In Row ',row,'Do it manually[block A]',s.cell(row,col).value
                        x=s.cell(row,col).value
                        Error=True
        while True:
            x=values.find('(at)')
            y=values.find('(dot)')
            try:
                if  x!=-1:
                    values=values[:x]+'@'+values[x+4:]
                if y!=-1:
                    values=values[:y-3]+'.'+values[y+2:]
            except:
                print 'error occured at row: ',row
                #print 'data:',s.cell(row,col).value
                Error=True
                break
            if x==-1 and y==-1:
                break
            
        ls=values.split('<')
        if(len(ls)>1 and not Error):
            try:
                count+=1
                res.write('||'.join(ls)+'\n')
            except:
                print 'Error In Row ',row,'Do it manually[block A]',s.cell(row,col).value
                print 'Data : '+' '.join(ls)+'len ls: '+str(len(ls))
        else:
            try:
                count+=1
                res.write(''+'||'+ls[0]+'\n')
            except:
                print 'Error In Row ',row,'Do it manually[block A]',s.cell(row,col).value
                print 'Data : '+' '.join(ls)+'len ls :' +str(len(ls))
                
        if count%100 ==0:
            print 'Email Harvested :',count
    res.write('Total Email Harvested : '+str(count))
    res.close()
    time.sleep(10)
