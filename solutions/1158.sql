-- Solution 1
SELECT
    u.user_id AS buyer_id,
    u.join_date,
    COALESCE(COUNT(o.order_id)) AS orders_in_2019
FROM users AS u
LEFT JOIN orders o ON o.buyer_id = u.user_id AND YEAR(o.order_date) = 2019
GROUP BY u.user_id, u.join_date
