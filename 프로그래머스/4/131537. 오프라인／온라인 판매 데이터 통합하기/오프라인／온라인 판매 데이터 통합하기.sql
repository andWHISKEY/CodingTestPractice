SELECT SALES_DATE,PRODUCT_ID,USER_ID,SALES_AMOUNT
FROM (SELECT date_format(SALES_DATE,'%Y-%m-%d') AS SALES_DATE,PRODUCT_ID, NULL AS USER_ID,SALES_AMOUNT
        FROM OFFLINE_SALE
        UNION ALL
        SELECT date_format(SALES_DATE,'%Y-%m-%d') AS SALES_DATE,PRODUCT_ID,USER_ID,SALES_AMOUNT
        FROM ONLINE_SALE) A
WHERE '2022-03-01'<=SALES_DATE AND SALES_DATE<='2022-03-31'
ORDER BY SALES_DATE , PRODUCT_ID, USER_ID