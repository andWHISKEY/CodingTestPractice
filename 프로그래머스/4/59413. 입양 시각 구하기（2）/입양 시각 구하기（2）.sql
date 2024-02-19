WITH RECURSIVE T AS (
    SELECT 0 AS HOUR
    UNION ALL
    SELECT HOUR+1 
    FROM T 
    WHERE HOUR<23
)

SELECT T.HOUR, COUNT(ANIMAL_ID) AS COUNT
FROM (SELECT *, HOUR(DATETIME) AS HOUR FROM ANIMAL_OUTS) A 
        RIGHT JOIN T ON A.HOUR=T.HOUR
GROUP BY T.HOUR
ORDER BY T.HOUR

# with recursive time as (
#     select 0 as hour
#     union all
#     select hour+1 from time where hour<23
# )

# select time.hour, count(animal_id) as count
# from (
#     select *, hour(datetime) as hour
#     from animal_outs) a
#     right join time on a.hour=time.hour
# group by time.hour
# order by time.hour