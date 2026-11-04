-- 4a. The Products table holds the items that Northwind sells.
-- 4b. The Categories table holds the types of items that Northwind sells.

USE northwind;

SELECT * FROM employees;
-- 5a. The employee whose name looks like a bird is Margaret Peacock.

SELECT * FROM products;
-- 6a. The products table has 77 records. To retrieve only 10 rows, use the "Limit to 1000 rows" dropdown in the toolbar and change it to "Limit to 10 rows".
-- 6b. (BONUS) To limit rows in the query itself, add LIMIT 10 at the end: SELECT * FROM products LIMIT 10; Source: MySQL 8.0 Reference Manual, SELECT Statement (dev.mysql.com).

SELECT * FROM categories;
-- 7. The CategoryID of Seafood is 8.
SELECT OrderID, OrderDate, ShipName, ShipCountry FROM orders LIMIT 50;