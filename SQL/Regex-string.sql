SELECT * FROM employee;

/*BASICS
^: Matches the start of the string.
$: Matches the end of the string.
[...]: Matches any single character within the brackets.
[A-C]: Matches any single character 'A', 'B', or 'C'.
.: Matches any single character.
*: Matches zero or more occurrences of the preceding element.
|: Alternation, matches either the expression before or after the |.
*/

/*Match any last name starting with 'A', 'B', or 'C'*/
SELECT * FROM employee WHERE last_name REGEXP '^[A-C]';

/*Match any last name containing 'oe' anywhere*/
SELECT * FROM employee WHERE last_name REGEXP 'oe';

/*Match any last name starting with 'D' or 'E' or 'S'*/
SELECT * FROM employee WHERE last_name REGEXP '^(D|E|S)';

/*Match any last name with exactly 5 characters*/
SELECT * FROM employee WHERE last_name REGEXP '^[A-Za-z]{5}';

/*Select employees whose first name starts with a vowel*/
SELECT * FROM employee WHERE first_name REGEXP '^[AEIOU]';

/* Select where first name starts with J followed by any one of two character and end with n*/
SELECT * FROM employee WHERE first_name REGEXP '^J..n$'

/*Select where first name end with hm*/
SELECT * FROM employee WHERE first_name REGEXP 'hn$';

/*Match last names that start with 'A', 'B', or 'C' and are followed by any number of characters*/
SELECT * FROM employee WHERE last_name REGEXP '^[A-C].*';

/*Select employees whose last name contains a digit*/
SELECT * FROM employee WHERE last_name REGEXP '[0-9]';


