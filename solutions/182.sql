-- Solution 1
SELECT email
FROM person
GROUP BY email
HAVING COUNT(email) >= 2