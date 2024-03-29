# -- 코드를 입력하세요
SELECT i.REST_ID,REST_NAME,FOOD_TYPE,FAVORITES,ADDRESS,ROUND(AVG(REVIEW_SCORE),2) AS SCORE
FROM REST_INFO AS i RIGHT OUTER JOIN REST_REVIEW AS r
# Inner Join=Join, Right Outer Join #Left Outer Join
ON i.REST_ID=r.REST_ID
# WHERE ADDRESS LIKE '서울%' # LIKE #IN (조건)
GROUP BY r.REST_ID
HAVING ADDRESS LIKE '서울%'
ORDER BY SCORE DESC ,FAVORITES DESC