# Write your MySQL query statement below
WITH A AS (SELECT employee_id, department_id
        FROM Employee
        Group by employee_id
        Having COUNT(distinct department_id)=1 
    Union
        SELECT employee_id, department_id
        FROM Employee
        Where primary_flag='Y'
        Group by employee_id
) 

Select *
From A
Order by employee_id
