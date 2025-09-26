# Write your MySQL query statement below
select v.customer_id, count(v.visit_id) as count_no_trans
from Visits v
left Join Transactions t
 ON v.visit_id = t.visit_id
 Where t.transaction_id Is null
 Group By v.customer_id