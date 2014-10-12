<?php
session_start();
require('dbconnect.php');
$handle = fopen("final.sua", "r");
if ($handle) {
	$lineno = (int)($_POST['start']);
    $Num_of_insert=0;
	$i=0;
	while (($i!=$lineno)&&(($line = fgets($handle)) !== false)) {
	$i++;
	}
    while (($line = fgets($handle)) !== false) {
	   $row_data=explode("<!|!>",$line);
	   
	   try{
	       // Here we have to insert 5 data in each row
		   //Change this query according to you
	      $q = $pdo->prepare('INSERT INTO `libcat` (publisher, title, doctype, subject, url) VALUES (?, ?, ?, ?, ?);');
	      $q->execute(array($row_data[1],$row_data[2],$row_data[3],$row_data[4],$row_data[5]));
		  $Num_of_insert++;
		  if($Num_of_insert == 10 || ($Num_of_insert+$i)>= $_SESSION['total'] ){
		    echo $Num_of_insert+$i;
			break;
		  }
		  
         }catch (Exception $e){
		    echo 'Error in row',$row_data[0];
            }
    }
} else {
    echo 'Error In opening File';
} 
fclose($handle);
?>