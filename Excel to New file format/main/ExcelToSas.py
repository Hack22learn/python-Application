# Process Excel File and write New Processed Data In New File format
# each field seperated with  <!|!>
#Remove all character with ascii value >128

from xlrd import open_workbook
import codecs
import sys


def trim(s):
    # Remove Extra Spaces
    ls=s.split(' ')
    for i in range(ls.count('')):
        ls.remove('')
    return ' '.join(ls)
def remove_anomaly(s):
    #Remove or replace data with ascii value greter than 128
    cell_data=''
    for ch in s:
        if ord(ch)==160:
            cell_data +=' '
        elif ord(ch)>256:
            cell_data +='-'
        else:
            cell_data +=chr(ord(ch))
    while(len(cell_data)>0 and (cell_data[0]==' ' or cell_data[-1]==' ')):
        if cell_data[0]==' ':
            cell_data=cell_data[1:]
        elif cell_data[-1]==' ' and len(cell_data)>0:
            cell_data=cell_data[:-1]
    return cell_data


f_name=raw_input('Enter Excel file name with extention :')
try:
    wb = open_workbook(f_name) #Open File to read
    try:
        res=open('final.sas','w') #Where Result Going to save
    except:
        print 'Error in opning result file'
except:
    print 'Error in opening file'

for s in wb.sheets(): # If More Than One Seet in Excel File , Even Then It process all data in all sheets
    print 'Sheet:',s.name
    for row in range(1,s.nrows): #for data in each row except the first row, as it is title of each row 
        values = []
        Error=False
        for col in range(s.ncols): #for data in in row=rowX and coloumn=col
            if col!=0: # then remove extra space  or ?
                try:
                    cell_data=str(s.cell(row,col).value)
                    cell_data=trim(cell_data)
                    values.append(cell_data)
                except:
                    try:
                        values.append(remove_anomaly(s.cell(row,col).value))
                    except:
                        print 'Error In Row ',row,'Do it manualy[block A]',s.cell(row,col).value
                        x=s.cell(row,col).value
                        Error=True
            else:
               try:
                   values.append(str(int(s.cell(row,col).value)))
               except:
                   print 'Error In Row ',row,'Do it manualy[block b]'
                   Error=True
                    
           # col +=1
        if(Error == False):
            res.write('<!|!>'.join(values)+'\n')
res.close()
print 'Good Bye we r done , Check ""final.sua""'
raw_input()
