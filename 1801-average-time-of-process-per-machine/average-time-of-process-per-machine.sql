with A as ( select machine_id,process_id,timestamp as start_time
            from Activity
            where activity_type='start'
)
, B as ( select machine_id,process_id,timestamp as end_time
            from Activity
            where activity_type='end'
)

# Write your MySQL query statement below
select A.machine_id, round((sum(end_time)-sum(start_time))/count(A.machine_id),3) as processing_time
from A inner join B on A.machine_id=B.machine_id and A.process_id=B.process_id
group by machine_id 