-- 2022년 1월의 도서 판매 데이터를 기준으로 저자 별, 카테고리 별 매출액(TOTAL_SALES = 판매량 * 판매가) 을 구하여
-- 저자 ID(AUTHOR_ID), 저자명(AUTHOR_NAME), 카테고리(CATEGORY), 매출액(SALES) 리스트를 출력
-- 결과는 저자 ID를 오름차순으로, 저자 ID가 같다면 카테고리를 내림차순 정렬
With A as (
    SELECT BOOK_ID,SUM(SALES) as TOTAL_SALES
    FROM BOOK_SALES
    WHERE '2022-01-01'<=SALES_DATE and SALES_DATE<='2022-01-31'
    GROUP BY BOOK_ID
),
B as (
    SELECT A.BOOK_ID, AUTHOR_ID,CATEGORY,PRICE*TOTAL_SALES as TOTAL_SALES
    FROM A left join BOOK on A.BOOK_ID=BOOK.BOOK_ID
),
C as (
    SELECT B.AUTHOR_ID,AUTHOR_NAME,CATEGORY,SUM(TOTAL_SALES) as TOTAL_SALES
    FROM B left join AUTHOR on B.AUTHOR_ID=AUTHOR.AUTHOR_ID
    GROUP BY AUTHOR_NAME,CATEGORY
)
select *
from C
ORDER BY AUTHOR_ID asc, CATEGORY desc

# SELECT AUTHOR_ID,AUTHOR_NAME,CATEGORY,TOTAL_SALES