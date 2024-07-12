SELECT * FROM employee;
ALTER TABLE employee ADD COLUMN email varchar(100) DEFAULT 'nkexample@gmail.com';
ALTER TABLE employee ADD COLUMN ph_no varchar(10) DEFAULT '8825731840';

/* pattern matching */

/*
Matching the Start of a String
Select employees whose first name starts with 'J'
*/
SELECT * FROM employee WHERE first_name LIKE 'J%';
/*we can match more than one also like first name starts with Jho*/
SELECT * FROM employee WHERE first_name LIKE 'joh%';


/*Matching the End of a String
Select employees whose last name ends with 'e'
*/
SELECT * FROM employee WHERE last_name LIKE '%e';
/*we can match more than one also like last name ends with th*/
SELECT * FROM employee WHERE last_name LIKE '%th';

/*Note : case in-sensitive hence j and J both same likewise for all*/

/* Matching Any Character
Select employees whose first name contains 'o' as the second character
*/
SELECT * FROM employee WHERE first_name LIKE '_o%';

/* Matching start char and end char*/
SELECT * FROM employee WHERE first_name LIKE 'E%y';

/* Selecting employee  where first_name length exactly 4*/
/* u have to use 4 underscores(-)*/
SELECT * FROM employee WHERE first_name LIKE '____';





