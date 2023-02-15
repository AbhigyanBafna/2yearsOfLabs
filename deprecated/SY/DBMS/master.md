# Important mysql commands

```mysql

-- COMMANDS

mysql -u root -p



-- BASIC QUERIES

-- Print Client master table
SELECT * FROM client_master;

-- Retrieve list of name, city of all Clients
SELECT name,city FROM client_master;

-- Find clients who have second letter 'a'.
SELECT name FROM client_master WHERE name LIKE '_a%';

-- Find clients who stay in city ending with letter 's'.
SELECT name,city FROM client_master WHERE city LIKE '%s';

-- Find list of clients who stay in Bombay or Madras.
SELECT name,city FROM client_master WHERE city = 'Bombay' OR city = 'Madras';

-- Print list of clients whose Bal Due is greater than 10K.
SELECT name FROM client_master WHERE bal_due > 10000;

-- Print info of orders placed in January.
SELECT * FROM sales_order WHERE (s_order_date LIKE '%-01-%');

-- Find product whose selling price is greater than 2000 and less than equal to 5000.
SELECT Description FROM Product_master WHERE Sell_price > 2000 AND Sell_price <= 5000;

-- Calculate new sell_price as (og sell_price * 0.15) and rename as New_price for products whose og sell_price > 5000.
SELECT Description, Sell_price*0.15 “NEW_PRICE” FROM PRODUCT_MASTER WHERE Sell_price > 5000;

-- List product in sorted order of their description.
SELECT Description FROM Product_master ORDER BY Description ASC;

-- Count the number of products having price less than 15000.
SELECT COUNT(*) FROM Product_master WHERE Sell_price >15000;

-- Calculate Avg, Min and Max of all Products.
SELECT MIN(Sell_price), MAX(Sell_price), AVG(Sell_price), AVG(Cost_price) FROM Product_master;

-- Calculate the Sqrt price of each Product.
SELECT SQRT(Sell_price) FROM Product_master;

-- Divide the cost of product '540 HDD' by difference between its price and 100.
SELECT Cost_price/(Cost_price - 100) AS Difference from product_master WHERE Description = 'HDD' ;


-- COMPLEX QUERIES

-- List orders cancelled in March.
SELECT * FROM sales_order WHERE order_status = 'c' AND order_date BETWEEN '1996-03-01' AND '1996-03-31';

-- Print description and total quantity sold for each product.
SELECT s.product_no, p.description, SUM(qty_ordered) FROM sales_order_details AS s, product_master AS p GROUP BY Product_no, p.Description;

-- Find product no and description of non-moving products.
SELECT Product_no, Description FROM Product_master WHERE Product_no NOT IN (SELECT Product_no FROM sales_order_details);

--Find customers name, city and pincode for client who placced order no '019001'.
SELECT Name, Address1, Address2, City, Pincode FROM Client_master WHERE Client_no IN (SELECT client_no FROM sales_order WHERE s_order_no = 'O19001');



--VIEWS, TRIGGERS AND CURSORS

--VIEWS
CREATE VIEW V1 AS SELECT client_no, name,city FROM client_master;
SELECT * FROM V1

--TRIGGERS
CREATE TABLE Student (roll_no int(2), name varchar(20), CGPA int(4), Commitee varchar(15));

delimiter $$
CREATE TRIGGER tg1
BEFORE INSERT ON student
FOR EACH ROW
BEGIN
SET NEW.name = upper(new.name);
SET NEW.Commitee = upper(new.commitee);
END;
$$
delimiter ;

INSERT INTO Student VALUES (1, 'aBHI', 9.87, 'iETE');
SELECT * FROM Student;

-- CURSORS
-- 1)
Delimiter $$
CREATE PROCEDURE CPr()
BEGIN
DECLARE done INT(10) DEFAULT 0;
DECLARE i varchar(20);
DECLARE n varchar(100);
DECLARE curs1 CURSOR FOR SELECT roll_no,name FROM Student;
DECLARE CONTINUE HANDLER FOR NOT FOUND SET done=1;
OPEN curs1;
read_loop:LOOP
FETCH curs1 INTO i,n;
IF done=1 THEN
LEAVE read_loop;
END IF;
SELECT i,n;
END loop read_loop;
CLOSE curs1;
end;
$$

CALL CPr(); $$

-- 2)
CREATE PROCEDURE c1()
BEGIN
DECLARE last_row int default 0;
DECLARE cname varchar(20);
DECLARE cgpa int;
DECLARE cur1 cursor for SELECT name,CGPA FROM student;
DECLARE CONTINUE HANDLER FOR NOT FOUND SET last_row =1;
OPEN cur1;
myloop:LOOP
FETCH cur1 INTO cname,cgpa;
IF last_row=1 THEN
SELECT 'no record found' AS "message";
LEAVE myloop;
END IF;
SELECT cname;
END LOOP myloop;
CLOSE cur1;
end;$$

CALL c1()$$



--PROCEDURES AND FUNCTIONS

--FUNCTIONS
Delimiter $$
CREATE FUNCTION proprice(sell_price double) RETURNS varchar(20)
DETERMINISTIC
BEGIN
DECLARE lvl varchar(20);
IF sell_price<1000 THEN
SET lvl='CHEAP';
ELSEIF sell_price>3000 THEN
SET lvl='EXPENSIVE';
END IF;
RETURN(lvl);
END;
$$

SELECT product_no,proprice(sell_price) from product_master; $$

-- PROCEDURES
-- 1)
Delimiter $$
CREATE PROCEDURE my_pro(IN client_no int)
BEGIN
SELECT * from Client_master LIMIT client_no;
END;
$$

CALL my_pro(4);$$

-- 2)
CREATE PROCEDURE mp_1(OUT Client_no int)
BEGIN
SELECT COUNT(*) INTO Client_no FROM Client_master;
END;$$

CALL mp_1(@a); 
SELECT @a;$$

```

https://programforamitystudent.blogspot.com/2009/11/plsqlall-programs.html

