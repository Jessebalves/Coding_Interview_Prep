-- Write a solution to find employees who have the highest salary in each of the departments.
-- Return the result table in any order.
-- The result format is in the following example.
select d.name as Department, 
e.name as Employee,
e.salary as Salary
from Employee e
join Department d 
on e.departmentID = d.id 
where salary = (select max(salary) from Employee where departmentId = d.id) and e.departmentId = d.id
group by e.name;
