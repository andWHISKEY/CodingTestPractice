# Write your MySQL query statement below
with A as (
    select user_id,0 as comfirm_zero
    from signups
),
B as (
    select user_id,count(*) as action_cnt 
    from confirmations
    group by user_id
),
C as (
    select user_id,count(*) as confirm_cnt
    from confirmations
    where action='confirmed'
    group by user_id
),
D as (
    select C.user_id, case when confirm_cnt != 0 then ROUND((confirm_cnt/action_cnt),2) 
                            else 0 end as confirmation_rate
    from B join C on B.user_id=C.user_id
)

select A.user_id, case when confirmation_rate is null then comfirm_zero 
                                            else confirmation_rate end as confirmation_rate
from A left join D on A.user_id=D.user_id