/*Select All Records from a Table*/
SELECT * FROM departments;
SELECT * FROM employee;

/* String operations*/

/* Concating the string */
SELECT CONCAT(first_name,' ',last_name) AS full_name FROM employee;

/* Substring (string,start_ind,end_ind)
Note : it is 1 based indexing
*/
SELECT SUBSTRING(first_name,1,4) AS short_name From employee;

/*Upper*/
SELECT UPPER(first_name) AS f_name FROM employee;
/*lower*/
SELECT LOWER(first_name) AS f_name FROM employee;

/*TRIM: 
Remove leading and trailing spaces
RTRIM:
Remove Trailing spaces
LTRIM
Remove Leading spaces
*/
SELECT TRIM(first_name) as f_name FROM employee;
SELECT RTRIM('NAVEEN   ') AS right_trimmed;
SELECT LTRIM('    NAVEEN') AS left_trimmed;

/*Length*/
SELECT LENGTH(first_name) AS length_of_fname FROM employee;

/*Replace*/
SELECT REPLACE(first_name,'John','Jonathan') AS f_name FROM employee;


/*
LEFT(): Extracts a specified number of characters from the left side of a string.
RIGHT(): Extracts a specified number of characters from the right side of a string.
*/
SELECT LEFT('EXAMPLE',3) AS first_three,RIGHT('EXAMPLE',3) AS  last_three;

/*POSITION(): Returns the position of the first occurrence of a substring in a string.*/
SELECT POSITION('AMP' IN 'EXAMPLE') AS A, POSITION('AME' IN 'EXAMPLE') as B;
