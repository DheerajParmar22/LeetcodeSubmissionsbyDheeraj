# Write your MySQL query statement below

SELECT name as customers from Customers WHERE id NOT IN (SELECT customerId from Orders)