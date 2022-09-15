-- Solution 1: MySQL
SELECT DISTINCT(l1.num) AS ConsecutiveNums
FROM logs l1
LEFT JOIN logs AS l2 on l1.id + 1 = l2.id
LEFT JOIN logs AS l3 on l1.id + 2 = l3.id
WHERE l3.num IS NOT NULL AND l1.num = l2.num AND l1.num = l3.num

-- Solution 2: MySQL LAG/LEAD
SELECT DISTINCT num as ConsecutiveNums
FROM (
    SELECT num, 
    LEAD(num) OVER (ORDER BY id) AS `lead`, 
    LAG(num) OVER (ORDER BY id) AS `lag`
    FROM logs
) l
WHERE num=`lead` and `lead`=`lag`
