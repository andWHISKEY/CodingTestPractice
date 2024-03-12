# Write your MySQL query statement below
with A as (
    select movierating.user_id,name,count(*) as cnt
    from movierating join users on movierating.user_id=users.user_id
    group by movierating.user_id
    order by cnt desc ,name asc
    LIMIT 1
),
B as (
    select movierating.movie_id,title,avg(rating) as avgrating
    from movierating join movies on movierating.movie_id=movies.movie_id
    where created_at LIKE '2020-02%'
    group by movierating.movie_id
    order by avgrating desc ,title asc
    LIMIT 1
)
select name as results
from A
union all
select title as results
from B