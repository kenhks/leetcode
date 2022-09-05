-- Solution 1
SELECT
    u.name AS name,
    COALESCE(SUM(r.distance), 0) AS travelled_distance
FROM users AS u
LEFT JOIN rides r ON u.id = r.user_id
GROUP BY u.id, u.name
ORDER BY travelled_distance DESC, u.name
