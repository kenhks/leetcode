-- Solution 1: MySQL LEAD/LAG
SELECT
    id,
    CASE
        WHEN id % 2 = 1 THEN LEAD(student, 1, student) OVER (ORDER BY ID)
        ELSE LAG(student) OVER (ORDER BY ID)
    END as student
FROM seat
ORDER BY id

-- Solution 2: MySQL Bitwise swap
SELECT
    s1.id, COALESCE(s2.student, s1.student) AS student
FROM
    seat s1
        LEFT JOIN
    seat s2 ON ((s1.id + 1) ^ 1) - 1 = s2.id
ORDER BY s1.id
