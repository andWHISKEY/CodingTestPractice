# 난 column 추가해서 풀려했는데, 여기선 그렇게 푸는게 아니라 CASE IF ELSE로 풀어야함. 아래는 에러 
# ALTER TABLE FOOD_ORDER ADD COLUMN 출고여부 varchar(100)
# OUT_DATE그대로 출력시 몇시몇분몇초가 나옴, 이때 DATE_FORMAT(OUT_DATE,'%Y-%m-%d')처리 필요
SELECT ORDER_ID,PRODUCT_ID,DATE_FORMAT(OUT_DATE,'%Y-%m-%d') AS OUT_DATE,
CASE WHEN OUT_DATE <= '2022-05-01' THEN '출고완료'
WHEN OUT_DATE > '2022-05-01' THEN '출고대기'
ELSE '출고미정' 
END AS '출고여부'
FROM FOOD_ORDER
ORDER BY ORDER_ID ASC