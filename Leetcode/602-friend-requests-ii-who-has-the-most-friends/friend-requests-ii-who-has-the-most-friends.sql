# Write your MySQL query statement below
with A as (
    select requester_id as id ,count(*) as num
    from requestaccepted
    group by requester_id
),
B as (
    select accepter_id as id, count(*) as num
    from requestaccepted
    group by accepter_id
),
C as (
    
    select A.id, A.num+(case when B.num is null then 0 else B.num end) as num
    from A left join B on A.id=B.id
    union
    select B.id,(case when A.num is null then 0 else A.num end)+B.num as num
    from A right join B on A.id=B.id
)
-- select *
-- from C
select id, num
from C
where num in (select max(num) from C) 