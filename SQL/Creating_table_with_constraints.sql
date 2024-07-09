/* example for creating a table with all constraints */
CREATE TABLE departments( department_id INT PRIMARY KEY,department_name varchar(100) UNIQUE NOT NULL);

INSERT INTO departments (department_id, department_name) VALUES (101, 'Human Resources');
INSERT INTO departments (department_id, department_name) VALUES (102, 'Finance');
INSERT INTO departments (department_id, department_name) VALUES (103, 'Engineering');
INSERT INTO departments (department_id, department_name) VALUES (104, 'Marketing');
INSERT INTO departments (department_id, department_name) VALUES (105, 'Sales');

/* making the department_id as foreign key in employee and also check the slary should be >0*/
CREATE TABLE employee(
emp_id int PRIMARY KEY,
first_name varchar(30) NOT NULL,
last_name varchar(30),
hire_date date NOT NULL,
salary decimal(10,2) check(salary>0),
dept_id int,
CONSTRAINT dep_id_fk
FOREIGN KEY(dept_id)
REFERENCES departments(department_id)
);

INSERT INTO employee (emp_id, first_name, last_name, hire_date, salary, dept_id) VALUES (1, 'John', 'Doe', '2020-01-15', 60000.00, 101);
INSERT INTO employee (emp_id, first_name, last_name, hire_date, salary, dept_id) VALUES (2, 'Jane', 'Smith', '2019-03-22', 70000.00, 102);
INSERT INTO employee (emp_id, first_name, last_name, hire_date, salary, dept_id) VALUES (3, 'Michael', 'Brown', '2021-07-11', 80000.00, 103);
INSERT INTO employee (emp_id, first_name, last_name, hire_date, salary, dept_id) VALUES (4, 'Emily', 'Davis', '2018-10-05', 75000.00, 104);
INSERT INTO employee (emp_id, first_name, last_name, hire_date, salary, dept_id) VALUES (5, 'Daniel', 'Wilson', '2017-11-20', 85000.00, 105);

/*Select All Records from a Table*/
SELECT * FROM departments;
SELECT * FROM employee;

/*Select Specific Columns*/
SELECT first_name, last_name FROM employee;

