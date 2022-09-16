-- Solution 1: MySQL LAG/LEAD
SELECT
    t.id,
    t.visit_date,
    t.people
FROM (
    SELECT 
        id,
        visit_date,
        people,
        LAG(people, 2) OVER (ORDER BY id) AS `day2before_people`,
        LAG(people, 1) OVER (ORDER BY id) AS `day1before_people`,
        LEAD(people, 1) OVER (ORDER BY id) AS `day1after_people`,
        LEAD(people, 2) OVER (ORDER BY id) AS `day2after_people`
    FROM stadium
) AS t
WHERE t.people >= 100
    AND (
        (t.day1after_people >= 100 AND t.day2after_people >= 100)
        OR (t.day1before_people >= 100 AND t.day2before_people >= 100)
        OR (t.day1before_people >= 100 AND t.day1after_people >=100)
    )
