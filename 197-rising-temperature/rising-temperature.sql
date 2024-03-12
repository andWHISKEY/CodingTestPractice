# Write your MySQL query statement below
With B AS (
 SELECT id,date_add(recordDate, INTERVAL -1 DAY) AS recordDate,temperature
 FROM Weather
)

SELECT B.id
FROM B AS B right join Weather AS A ON DATE_FORMAT(A.recordDate,'%Y-%m-%d')=DATE_FORMAT(B.recordDate,'%Y-%m-%d')
WHERE B.temperature > A.temperature
