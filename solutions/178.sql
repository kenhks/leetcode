-- Solution 1: MySQL
SELECT
    s.score,
    DENSE_RANK() OVER (ORDER BY s.score DESC) AS 'rank'
FROM scores AS s
