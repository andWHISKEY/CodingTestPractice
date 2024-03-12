# Write your MySQL query statement below

with recursive B as (
    select 1 as n,CAST('Low Salary' AS CHAR(20)) as category, 0 as cnt
    union all
    select n+1, case when n=1 then 'Average Salary' when n=2 then 'High Salary' end as category,0 as cnt
    from B
    where n<3
), 
A as (select account_id,income,case when income<20000 then 'Low Salary'when income>50000 then 'High Salary'when 20000<=income<=50000 then 'Average Salary' end as category,count(*) as accounts_count
    from accounts
    group by category)



select B.category, case when accounts_count is null then B.cnt when accounts_count is not null then A.accounts_count end as accounts_count
from A right join B on A.category=B.category
group by B.category
