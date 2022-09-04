-- Solution 1
SELECT player_id, MIN(event_date) AS first_login
FROM activity
GROUP BY player_id
