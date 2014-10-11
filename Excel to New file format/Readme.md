Requirement: 
       ->Python 2.7
	   ->Python Module ""xlrd""
_____________________________________________________________
create A system to upload data to your website in some text type file 
which can directly insert to database
____________________________________ ________________________
""ExcelToSua"" : 
Read Excel file and Remove all data with ascii value greter then
128 by '_' .
and data with ascii value ==160 by a space character
and save result is our require formated data in ""final.sua""
_____________________________________________________________ 
"file.php" : read ""final.sua"" line by line and split it in columns
similar to as in excel file then insert it to database.

Note: database prototype should be created before above operation
Nore : You need to modify code according to your need  

