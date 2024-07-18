SELECT * FROM employee;
/*
GROUPBY:
	The GROUP BY clause groups rows that have the same values into summary rows. 
	This is often used with aggregate functions (COUNT, SUM, AVG, MAX, MIN).
HAVING:
	The HAVING clause is used to filter groups based on specific conditions, similar to the WHERE clause but for groups.
*/

/*GROUP BY */
/*Example 1: Count of Employees in Each Department*/
SELECT COUNT(*) AS total_employees FROM employee GROUP BY dept_id;

/*EXAMPLE 2: Average Salary in Each Department*/
SELECT AVG(salary) AS average_salary FROM employee GROUP BY dept_id;

/*Example 3: Total Payroll per Department*/
SELECT SUM(salary) AS total_payroll FROM employee GROUP BY dept_id;

/*Example 4: Maximum Salary in Each Department*/
SELECT MAX(salary) AS max_salary FROM employee GROUP BY dept_id;

/* HAVING clause */

/*Example 1: Departments with More Than 2 Employees*/
SELECT * FROM employee GROUP BY dept_id HAVING COUNT(*)>2;

/*Example 2: Departments with an Average Salary Greater Than 70,000*/
SELECT first_name,last_name,AVG(salary) FROM employee GROUP BY dept_id HAVING AVG(salary)>70000;

/*Example 3: Departments with Maximum Salary Less Than 80,000*/
SELECT first_name,dept_id FROM employee GROUP BY dept_id HAVING MAX(salary)<80000;


/*Using GROUP BY and HAVING with String Operations*/

/*Example 1: Count of Employees Grouped by First Letter of Last Name*/
SELECT first_name,last_name FROM employee GROUP BY LEFT(last_name,1);

