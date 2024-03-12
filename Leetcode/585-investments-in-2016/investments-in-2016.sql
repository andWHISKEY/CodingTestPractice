with A as (
    select tiv_2015
    from insurance
    group by tiv_2015
    having count(*)>1
),
B as (
    select lat,lon
    from insurance
    group by lat,lon
    having count(*)=1
)

# Write your MySQL query statement below
select ROUND(sum(tiv_2016),2) as tiv_2016
from insurance
where tiv_2015 in (select * from A) and (lat,lon) in (select lat,lon from B)