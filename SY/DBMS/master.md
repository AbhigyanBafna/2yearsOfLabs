# Important mysql commands

```mysql

-- COMMANDS

mysql -u root -p -- Used to Start mysql



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
SELECT Description FROM Product_master ORDER BY Description;

-- Count the number of products having price less than 15000.
SELECT COUNT(*) FROM Product_master WHERE Sell_price >15000;

-- Calculate Avg, Min and Max of all Products.
SELECT MIN(Sell_price), MAX(Sell_price), AVG(Sell_price), AVG(Cost_price) FROM Product_master;

-- Calculate the Sqrt price of each Product.
SELECT SQRT(Sell_price) FROM Product_master;



-- COMPLEX QUERIES

-- List orders cancelled in March.
SELECT * FROM sales_order WHERE order_status = 'c' AND order_date BETWEEN '1996-03-01' AND '1996-03-31';

-- Print description and total quantity sold for each product.
SELECT s.product_no, p.description, SUM(qty_ordered) FROM sales_order_details AS s, product_master AS p GROUP BY Product_no, p.Description;

-- Find product no and description of non-moving products.
SELECT Product_no, Description FROM Product_master WHERE Product_no NOT IN (SELECT Product_no FROM sales_order_details);

--Find customers name, city and pincode for client who placced order no '019001'.
SELECT Name, Address1, Address2, City, Pincode FROM Client_master WHERE Client_no IN (SELECT client_no FROM sales_order WHERE s_order_no = 'O19001');

```

https://programforamitystudent.blogspot.com/2009/11/plsqlall-programs.html

