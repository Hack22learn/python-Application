<?php
require('dbconnect.php');
$handle = fopen("final.sua", "r");
if ($handle) {
    while (($line = fgets($handle)) !== false) {
	   $row_data=explode("<!|!>",$line);
	   
	   try{
	       // Here we have to insert 5 data in each row
		   //Change this query according to you
	      $q = $pdo->prepare('INSERT INTO libcat (publisher, title, doctype, subject, url) VALUES (?, ?, ?, ?, ?);');
	      $q->execute(array($row_data[1],$row_data[2],$row_data[3],$row_data[4],$row_data[5]));
         }catch (Exception $e){
		    echo 'Error in row',$row_data[0];
            }
    }
} else {
    echo 'Error In opening File';
} 
fclose($handle);
?>