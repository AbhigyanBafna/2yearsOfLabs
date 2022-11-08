# Structured Query Language(SQL)

| DDL         | DML         | DCL         | TCL         | Constraints |
| ----------- | ----------- | ----------- | ----------- | ----------- |
| Create      | Select      | Grant       |Commit       | Primary Key |
| Alter       | Insert      | Revoke      |Rollback     | Foreign Key |
| Drop        | Update      |             |Savepoint    | Check       |
| Truncate    | Delete      |             |             | Unique      |
| Rename      |             |             |             | Default     |
|             |             |             |             | Not Null    |


<br>

## Data Definition Language(DDL)

* DDL commands are used to perform various operations on the structure/schema of the Database.
  *  <b>CREATE</b> is used for creation of a table.
  *  <b>ALTER</b> is used to modify/drop/add existing columns and constraints in a table. It can also be used for renaming them.
  *  <b>DROP</b> deletes the whole table with its contents entirely. Cannot ROLLBACK.
  *  <b>TRUNCATE</b> Keeps the column headings and deletes all the data(tuples) in the table. Cannot ROLLBACK.
  *  <b>RENAME</b> used to Rename columns or even the whole table. 
<br><br>
<b>Link to Code : </b>[DDL](https://github.com/AbhigyanBafna/collegeLabs/blob/main/SY/DBMS/DDL.md)    


## Data Manipulation Language(DML)

* DML commands are used to perform various operations on the data inside the Database.
  *  <b>SELECT</b> 
  *  <b>INSERT</b> 
  *  <b>UPDATE</b> is used to modify or perform calculations on the data.
  *  <b>DELETE</b> works like truncate but a WHERE clause can select and delete specific tuples according to user. ROLLBACK possible before COMMIT.


## Data Control Language(DCL)

* DCL commands are used to control various privilages to different users of the Database.
*  


## Transactional Control Language(TCL)

* TCL commands are used to control transactions in the Database. Assists in implementing ACID
properties.
*  


## Constraints

* Often we need to ensure that data in our database follows some set of rules specified by us.
Constraints let us to implement these rules on the data.
  *  <b>PRIMARY KEY</b> UNIQUE + NOT NULL.
  *  <b>FOREIGN KEY</b> assists in referencing between two tables.
  *  <b>CHECK</b> checks if the input is inside the user defined domain.
  *  <b>UNIQUE</b> does not let duplicate values exist in that column.
  *  <b>DEFAULT</b> assigns a user defined value by default to that column.
  *  <b>NOT NULL</b> makes it compulsory to enter some value.


