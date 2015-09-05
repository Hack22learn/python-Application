
import MySQLdb
import time

host='localhost'
username='root'
password=''
database='trai'
try:
    db = MySQLdb.connect(host,username,password,database)
except:
    print 'Unable to connect to database check your Username ,password, databasename or hostname'
    exit()
f_name=raw_input('Enter Text file name>>>')
#day=raw_input('Enter tabe name>>')
try:
    f=open(f_name,'r')
    err=open('Error.txt','w')
except:
    print 'Unable to open file',f_name
    exit()

cursor=db.cursor()
count=0
error=0
for ln in f:
    try:
        ls=ln.split('||')
        #sql="INSERT INTO `day0`(`name`, `email`) VALUES ('"+ls[0]+"','"+ls[1]+"');"
        #sql="""INSERT INTO anooog1 (`name`,`email`) VALUES (%s,%s)""",(ls[0],ls[1])
        #cursor.execute(sql)
        cursor.execute("""INSERT INTO `day0` (`name`,`email`) VALUES (%s,%s)""",(ls[0],ls[1]))
        db.commit()
        count+=1
        if count % 100==0:
            print 'Insertion Count :',count
            #time.sleep(5)
    except:
        db.rollback()
        print 'Error :',ln
        try:
            err.write(ln)
        except:
            print 'Unable to write in error file'
        error+=1
        if error%10==0:
            print 'Error count: ',error
        
err.close()
db.close()
f.close()
time.sleep(10)
