-- Solution 1: MySQL
SELECT
    t.request_at AS 'Day',
    ROUND(
        COUNT(
            CASE 
                WHEN t.status = 'cancelled_by_driver' OR t.status = 'cancelled_by_client' THEN t.id
                ELSE NULL
            END
        ) / COUNT(*), 2
    ) AS 'Cancellation Rate'
FROM trips AS t
LEFT JOIN users u1 ON t.client_id = u1.users_id AND u1.role = 'client'
LEFT JOIN users u2 ON t.driver_id = u2.users_id AND u2.role = 'driver'
WHERE u1.banned = 'No' and u2.banned = 'No' AND t.request_at BETWEEN "2013-10-01" AND "2013-10-03"
GROUP BY t.request_at
