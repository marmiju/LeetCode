# Write your MySQL query statement below
SELECT name, population, area 
FROM world
WHERE population >= 25000000 
  or area >= 3000000;
