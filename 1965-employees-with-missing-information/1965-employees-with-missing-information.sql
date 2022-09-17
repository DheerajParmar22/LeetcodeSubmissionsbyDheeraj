# Write your MySQL query statement below

SELECT employee_id from Employees where employee_id not in (SELECT employee_id from Salaries)
UNION
SELECT employee_id from Salaries where employee_id not in (SELECT employee_id from Employees)
order by employee_id