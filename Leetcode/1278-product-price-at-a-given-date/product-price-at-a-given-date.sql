with A as (
    select product_id,10 as original_price
    from products
    group by product_id
)
,B as (select product_id,new_price
       from Products
       Where (product_id,change_date) in (select product_id,max(change_date) as change_date from Products where change_date<='2019-08-16' group by product_id)
       group by product_id
        )
-- select *
-- from B        
# Write your MySQL query statement below
Select A.product_id, case when new_price is null then original_price when new_price is not null then new_price end as price 
from B right join A on A.product_id=B.product_id
