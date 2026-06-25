# Write your MySQL query statement below
select emp.name as Employee from Employee emp join Employee man on emp.managerId = man.id where emp.salary>man.salary 