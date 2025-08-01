# Write your MySQL query statement below
select pd.product_name , s.year, s.price from Sales s inner join Product pd on s.product_id = pd.product_id