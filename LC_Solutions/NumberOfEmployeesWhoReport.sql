/* Write your MySQL query statement below */
select e2.employee_id, e2.name, 
count(e1.reports_to) as reports_count, 
round(avg(e1.age),0) as average_age 
from Employees e1
join Employees e2 on e2.employee_id = e1.reports_to and e1.reports_to is not null
group by e2.employee_id
order by e2.employee_id;
