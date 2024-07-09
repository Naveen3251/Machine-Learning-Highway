/*Select All Records from a Table*/
SELECT * FROM departments;
SELECT * FROM employee;

/*Aggregate functions perform a calculation on a set of values and return a single value.*/

/* COUNT */
/* counting total employee*/
SELECT COUNT(*) AS total_employee FROM employee;

/* SUM */
/* calculate total payroll */
SELECT SUM(salary) AS total_payroll FROM employee;

/* AVG *?
/* calculate average salary */
SELECT AVG(salary) AS avg_salary FROM employee;

/* MIN */
SELECT MIN(salary) AS lowest_salary FROM employee;

/* MAX */
SELECT MAX(salary) AS maximum_salary FROM employee;