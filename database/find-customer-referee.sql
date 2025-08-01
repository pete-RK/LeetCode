# Write your MySQL query statement below
select name from Customer as cm where cm.referee_id != 2 or cm.referee_id is null;