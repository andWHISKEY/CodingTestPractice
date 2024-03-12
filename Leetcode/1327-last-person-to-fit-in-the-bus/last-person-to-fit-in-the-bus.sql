# Write your MySQL query statement below
with A as (Select *,sum(weight) over(order by turn) AS total_weight
            from Queue)

select person_name
from A
where total_weight=(select max(total_weight) as total_weight from A where total_weight<=1000)


