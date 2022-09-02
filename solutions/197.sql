-- Solution 1
SELECT w2.id
FROM weather w1
JOIN weather w2 ON DATEDIFF(w2.recordDate, w1.recordDate) = 1
WHERE w2.temperature > w1.temperature
