-- This is MySql ... but strangely I started to know (MariaDB) Database first ... It was a fork of MySql and pre installed in Kali linux ...
-- It is 18 th December ... and this is Alexandro ... or known as Lexan Hacker ...
-- Fun Fact I really though I was using MongoDb because I saw it somewhere while I was using MariaDB ...

SELECT title FROM publications WHERE author = "Charles Dickens" ;

-- This essentially tells the myslq to select title table from a database called publications where the author is that name 

-- Commands that i will be learning ...
-- 1. mysql -u root -p 
-- 2. SHOW databases ; // this shows you the databases that you have  // it also uses the ; syntax like php 
-- 3. \c is for cancelling a command when you are half way and want to leave it ...
/* 4. Command Action
ALTER Alter a database or table
BACKUP Backup a table
\c Cancel input
CREATE Create a database
DELETE Delete a row from a table
DESCRIBE Describe a table’s columns
DROP Delete a database or table
EXIT (CTRL-C) Exit
GRANT Change user privileges
HELP (\h, \?) Display help
INSERT Insert data
LOCK Lock table(s)
QUIT (\q) Same as EXIT
RENAME Rename a table
SHOW List details about an object
SOURCE Execute a file
STATUS (\s) Display the current status
TRUNCATE Empty a table
UNLOCK Unlock table(s)
UPDATE Update an existing record
USE Use a database

// I just copied and pastied it from a book .... It is an amazing boo by the way ...


*/

/*

CREATE DATABASE lexan ;

USE lexan ;

CREATE TABLE deodata ( 
		firstname VARCHAR(128) , // ; this is a mistake as it will terminate and process the commands while incomplete ...
		lastname VARCHAR(128) ,
		age CHAR(2) ,
		year_born CHAR(4)) ; // this creates the table in the database ...

DESCRIBE deodata ; // this shows the form and datatype of the table ...

SHOW tables ; // shows all of the tables on your database ...

SELECT * FROM deodata ; // this shows all of the collumns and the records of the table called deodata ...

DROP TABLE deodata ; // This is the danger as it deletes the whole table of the database ...

Also the ALTER command is used to change vsrious things of the table like its name , columns and so on ...

ALTER TABLE deodata ADD ID INT UNSIGNED NOT NULL AUTO_INCREMENT KEY ; ..

SELECT something FROM tablename ; // this is used for querying of a database table for finding of information ...

DELETE FROM deodata WHERE first_name="pendo" ; // used for deleting a row with the first name of pendo ...

funfact ... WHERE is the Heart and Soul of SQL ...







*/