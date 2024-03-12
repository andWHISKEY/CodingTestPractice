# Write your MySQL query statement below
SELECT C.customer_id
FROM Customer C, Product P
WHERE C.product_key in (P.product_key)
GROUP BY C.customer_id
HAVING COUNT(Distinct C.product_key)=(SELECT COUNT(*) From Product) 
