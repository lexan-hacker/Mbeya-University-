<?php 

// This is a php code for dropping a table called trash from a database ...

// WHhat is magic here is that there is no any php file with the login details linked ... 

// Here we want to see if we can connect to the MySql Server at the hostname and with the credentials provided with the linked php file
$db_server = mysql_connect( $db_hostname , $db_username , $db_password ) ;

// Here it checks if you can  connect to your MySql server ... I not it exits with die() function and shows mysql error message ...
if ( !$db_server ) die( " Unable to connect to the MySql : " . mysql_error( ) ) ;

//here we check if we can connect to the database provided from the linked php file ... if not it exits and throws error messages ...
mysql_select_db( $db_database) 
	or die( "Unable to connect to the database : " . mysql_error() ) ;

//here the query variable is made with the sql statements that we want to make ...
$query = " DROP TABLE trash " ;	// there is no need for semicolon here ...

// the query variable is passed into mysql_query( ) which will handle it and make the statements to the database ... and the results are 
// passed into $result variable ...
$result = mysql_query($query) ;

// now here we check the $result variable to see if there was an error with out database statements ...
if ( !$result ) die( " Unable to delete the table , Permission denied : " . mysql_error( ) ) ;



?>