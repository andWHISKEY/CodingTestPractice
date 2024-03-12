# Write your MySQL query statement below
# department id기준으로 department join 해줌
with A as (
    select E.id,E.name,D.name as Department, salary, dense_rank() over (partition by D.name order by salary desc) as salary_rank
    from Employee E join Department D on D.id=E.departmentID
)

select Department,name as Employee,Salary#,salary_rank
from A
where salary_rank<=3
order by department , salary desc