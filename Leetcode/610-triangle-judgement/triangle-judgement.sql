# Write your MySQL query statement below
SELECT x,y,z,case when greatest(x,y,z)=x and y+z>x then 'Yes' when greatest(x,y,z)=y and x+z>y then 'Yes' when greatest(x,y,z)=z and x+y>z then 'Yes' Else 'No' End AS triangle
FROM Triangle


