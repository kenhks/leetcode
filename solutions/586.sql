-- Solution 1
SELECT customer_number
FROM orders
GROUP BY customer_number
ORDER BY COUNT(order_number) DESC
LIMIT 1

-- Solution 2
SELECT customer_number
FROM orders
GROUP BY customer_number
HAVING count(order_number) =
    (
        SELECT max(COUNT)
        FROM
        (SELECT count(order_number) AS COUNT,
                customer_number
        FROM orders
        GROUP BY customer_number) sub1
    )
