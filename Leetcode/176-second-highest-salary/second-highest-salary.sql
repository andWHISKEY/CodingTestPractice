# Write your MySQL query statement below 
#CASE WHEN salary IS NULL THEN 'null' ELSE salary END

select MAX(salary) AS SecondHighestSalary
from (select salary,dense_rank() OVER (ORDER BY salary desc) as ranking from Employee) E
where ranking=2