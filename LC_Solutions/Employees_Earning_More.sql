#id is the primary key (column with unique values) for this table.
#Each row of this table indicates the ID of an employee, their name, salary, and the ID of their manager.

# Write your MySQL query statement below
SELECT e1.name AS Employee FROM Employee e1
JOIN Employee e2 ON e1.managerId = e2.id
WHERE e1.salary > e2.salary;
