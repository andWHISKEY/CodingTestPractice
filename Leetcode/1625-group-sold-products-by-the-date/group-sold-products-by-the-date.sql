# Write your MySQL query statement below
with A as (
select *
from Activities
group by sell_date,product
order by sell_date
)

select sell_date,count(*) as num_sold,GROUP_CONCAT(distinct product SEPARATOR ',') as products
from A
group by sell_date