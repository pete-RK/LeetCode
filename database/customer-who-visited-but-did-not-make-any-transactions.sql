# Write your MySQL query statement below
select v.customer_id, count(v.visit_id) as count_no_trans 
from Visits v
Left Join Transactions t 
On v.visit_id = t.visit_id
Where t.transaction_id is NULL
group by v.customer_id;

