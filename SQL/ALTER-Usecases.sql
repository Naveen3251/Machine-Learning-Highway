/*creating the table */
CREATE TABLE NK(
id int,
firstname varchar(50),
lastname varchar(50),
join_data date,
salary decimal(10,2),
is_active boolean,
profile_picture blob
);
/*inserting the values*/
INSERT INTO Nk(id,firstname,lastname,join_data,salary,is_active,profile_picture) VALUES(1,'naveen','kumar','2024-01-09',12387908.89,false,null);

/*display*/
SELECT * FROM Nk;

/* adding column or columns*/
ALTER TABLE Nk ADD COLUMN promotion bool;
ALTER TABLE Nk ADD COLUMN (hi bool,bi bool);
/*dropping the column or columns*/
ALTER TABLE Nk DROP COLUMN profile_picture;
ALTER TABLE Nk DROP COLUMN hi, DROP COLUMN bi;

/*renaming the column*/
ALTER TABLE Nk RENAME COLUMN is_active TO isactive;

/*renaming the table name*/
ALTER TABLE Nk RENAME TO Nkgrp;
SELECT * FROM Nkgrp;

/*adding column with defaukt value*/
ALTER TABLE Nkgrp ADD COLUMN age int DEFAULT 100;
/* dropping that default*/
ALTER TABLE Nkgrp ALTER COLUMN age DROP DEFAULT;

/*changing columns definition*/
ALTER TABLE Nkgrp MODIFY COLUMN firstname varchar(100);