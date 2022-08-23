-- Solution 1
SELECT product_id
FROM   products
WHERE  low_fats = 'Y'
       AND recyclable = 'Y'
