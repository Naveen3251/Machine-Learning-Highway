/*Select All Records from a Table*/
SELECT * FROM departments;
SELECT * FROM employee;

/*Filtering based on comparision operators*/
/*Comparison operators include =, !=, <, >, <=, >=, BETWEEN, IN, and LIKE*/

/* Select the emp names whose hire date is 2021-07-11 */
/* = */
SELECT first_name,last_name FROM employee WHERE hire_date='2021-07-11';

/*Select the emp names whose hire date is not equal to 2021-07-11 */
/*  != */
SELECT first_name,last_name FROM employee WHERE hire_date!='2021-07-11';

/* select the employees whose salary is >70000 */
SELECT * FROM employee WHERE salary>70000;
/* as above query u can use < >= <= */

/*Select employees with salary between 60000 and 80000 */
SELECT * FROM employee WHERE salary BETWEEN 60000 and 80000;
SELECT * FROM employee WHERE salary>=60000 and salary<=80000;
/* both the above works well */

/* select particular ids */
/* IN operator*/
SELECT * FROM employee WHERE emp_id IN (1,3,4);

/* LIKE operator used for pattern matching */
/*Select employees whose first_name starts with 'J'
*/
SELECT first_name, last_name FROM employee WHERE first_name LIKE 'J%';

/*checking for null*/
SELECT * FROM employee WHERE last_name IS NOT NULL;

