-- Write a solution to find the names of all the salespersons who did not have any orders related to the company with the name "RED".
--Return the result table in any order.
--The result format is in the following example.
select s.name from SalesPerson s 
where s.name not in(select sp.name from SalesPerson sp 
join Orders o on sp.sales_id = o.sales_id
join Company c on c.com_id = o.com_id and c.name = 'RED');
