 <?php
    $host = 'localhost';
    $db_name = 'project1'; 
    $db_username = 'root'; 
    $db_password = '';
     // used to connect to database
    try
    {
        $pdo = new PDO('mysql:host='. $host .';dbname='.$db_name, $db_username, $db_password);
    }
    catch (PDOException $e)
    {
        exit('Error Connecting To DataBase');
    }?>