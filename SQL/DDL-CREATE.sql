/*DDL : CREATE */
CREATE TABLE NkGroup(
	emp_id int PRIMARY KEY,
	exployeename varchar(50),
    hire_data date
);
/* To insert the values*/
INSERT INTO NkGroup(emp_id,exployeename,hire_data) VALUES(123,'Naveen','2024-05-06');

/*Display*/
SELECT * FROM NkGroup;