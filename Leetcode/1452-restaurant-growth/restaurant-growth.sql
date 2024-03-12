with A as (
    select visited_on,sum(amount) as amount
    from customer
    Group by visited_on
),
B as (
    select visited_on,
    SUM(amount) OVER (order by visited_on rows between 6 preceding and current row) as amount,
    ROUND(SUM(amount) OVER (order by visited_on rows between 6 preceding and current row)/7,2) as average_amount,
    Rank() OVER (order by visited_on) as ran
    from A
)

-- select *
-- from B

# Write your MySQL query statement below
select visited_on,amount,average_amount
from B
where ran>=7