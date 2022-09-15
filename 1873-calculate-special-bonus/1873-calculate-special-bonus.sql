# Write your MySQL query statement below

SELECT employee_id, 
IF (employee_id%2 != 0 and name not LIKE "M%",salary,0) AS bonus 
from Employees 
ORDER BY employee_id 

# where mod(employee_id,2)!=0 and name not LIKE M% 