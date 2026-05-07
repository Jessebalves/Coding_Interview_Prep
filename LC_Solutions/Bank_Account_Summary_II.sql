-- Write a solution to report the name and balance of users with a balance higher than 10000.
-- The balance of an account is equal to the sum of the amounts of all transactions involving that account.
-- Return the result table in any order. 
-- Write your MySQL query statement below
select u.name as NAME,
sum((t.amount)) as BALANCE
from Users u join Transactions t
on t.account = u.account group by u.account having sum(t.amount) > 10000; 
