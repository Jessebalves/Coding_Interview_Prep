# Write your MySQL query statement below
# Runtime 674 ms (Beats 74.46%)
select product_name, sum(unit) as unit
from Products p
join Orders o on p.product_id = o.product_id
and o.order_date between timestamp('2020-02-01') and ('2020-02-29')
group by product_name having sum(unit) >= 100;
