Copy and Execute in MySQL. Creates a Database and executes DDL commands with a table named Student.

```
CREATE database Abhi_server;

USE Abhi_server;

CREATE table student(Name varchar(40) NOT NULL, Roll_No int, Stipend int, CGPA int, Branch varchar(5) NOT NULL, Year varchar(5));

SHOW tables;

DESC student;

ALTER table student ADD PRIMARY KEY(Roll_No);

ALTER table student add Commitee varchar(30);

ALTER table student DROP column year;

ALTER table student modify column name varchar(35) NOT NULL;

ALTER table student modify CGPA int NOT NULL;

ALTER table student RENAME dazeb;
ALTER table dazeb RENAME student;
```
