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

-- Find list of clients who stau in Bombay or Madras.
SELECT name,city FROM client_master WHERE city = 'Bombay' OR city = 'Madras';

--

```
