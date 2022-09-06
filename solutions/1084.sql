-- Solution
SELECT p.product_id, p.product_name
FROM product AS p
INNER JOIN sales AS s ON p.product_id = s.product_id 
GROUP BY p.product_id, p.product_name
HAVING MIN(s.sale_date) >= '2019-01-01' 
    AND MAX(s.sale_date) < '2019-04-01'
