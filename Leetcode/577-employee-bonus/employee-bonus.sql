# Write your MySQL query statement below
SELECT name, bonus
FROM Employee e left join Bonus b ON e.empID=b.empID
WHERE bonus<1000 or bonus is null