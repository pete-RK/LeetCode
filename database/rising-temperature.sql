-- Write your PostgreSQL query statement below
select today.id
from Weather yesterday
cross join Weather today

where today.recorddate - yesterday.recorddate =  1
and today.temperature  > yesterday.temperature;