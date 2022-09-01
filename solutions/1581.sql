-- Solution 1
SELECT
    v.customer_id, COUNT(v.visit_id) AS count_no_trans
FROM visits v 
LEFT JOIN transactions t
    ON t.visit_id = v.visit_id
WHERE t.visit_id IS NULL
GROUP BY v.customer_id
ORDER BY COUNT(t.transaction_id) DESC
