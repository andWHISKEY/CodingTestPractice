with A as (
    SELECT DISTINCT user_id,activity_date
    FROM Activity
    WHERE 0<=DATEDIFF('2019-07-27',activity_date) and DATEDIFF('2019-07-27',activity_date)<30 
)
select activity_date as day, count(*) as active_users
from A
group by activity_date
