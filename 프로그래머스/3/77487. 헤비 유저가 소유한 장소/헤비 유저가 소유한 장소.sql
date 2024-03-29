-- 코드를 입력하세요
# SELECT ID, NAME, HOST_ID
# FROM (SELECT ID,NAME,HOST_ID FROM PLACES GROUP BY HOST_ID HAVING COUNT(*)>1) A
# ORDER BY ID ASC

# SELECT 필드명, count(*)  FROM 테이블명 GROUP BY 필드명 HAVING count(*) > n;
# 출처: https://link2me.tistory.com/728 [소소한 일상 및 업무TIP 다루기:티스토리]
SELECT ID, NAME, HOST_ID
FROM PLACES
WHERE HOST_ID IN (SELECT HOST_ID FROM PLACES GROUP BY HOST_ID HAVING COUNT(*)>1)
ORDER BY ID ASC
