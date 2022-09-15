-- Solution 1: MySQL
SELECT 
    *
FROM cinema AS c
WHERE c.id % 2 = 1 AND c.description != 'boring'
ORDER by c.rating DESC
