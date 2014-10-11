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

f_name=raw_input('Enter Excel file name with extention :')
try:
    wb = open_workbook(f_name) #Open File to read
    try:
        res=open('final.sua','w') #Where Result Going to save
    except:
        print 'Error in opning result file'
except:
    print 'Error in opening file'

for s in wb.sheets(): # If More Than One Seet in Excel File , Even Then It process all data in all sheets
    print 'Sheet:',s.name
    for row in range(1,s.nrows): #for data in each row except the first row, as it is title of each row 
        values = []
        col=0
        for col in range(s.ncols): #for data in in row=rowX and coloumn=col
            if col == 1 or col==2: # then remove extra space  or ?
                try:
                    cell_data=str(s.cell(row,col).value)
                    cell_data=trim(cell_data)
                    values.append(cell_data)
                except:
                    try:
                        cell_data=''
                        for ch in u'%s'%(s.cell(row,col).value):
                            if ord(ch)<=128:
                                cell_data +=ch
                            elif ord(ch)==160:
                                cell_data +=' '
                            else:
                                cell_data +='_'
                        values.append(cell_data)
                    except:
                        print s.cell(row,col).value,'Aww! Ful'
            else:
                if col==0:
                    values.append(str(int(s.cell(row,col).value)))
                else:
                    try:
                        values.append(str(s.cell(row,col).value))
                    except:
                        try:
                            cell_data=''
                            for ch in u'%s'%(s.cell(row,col).value):
                                if ord(ch)<=128:
                                    cell_data +=ch
                                elif ord(ch)==160:
                                    cell_data +=' '
                                else:
                                    cell_data +='_'
                            values.append(cell_data)
                        except:
                            print s.cell(row,col).value,'Aww! Ful Others'
            col +=1
        res.write('<!|!>'.join(values)+'\n')
res.close()
print 'Good Bye we r done , Check ""final.sua""'
raw_input()
