-- Solution 1
SELECT sell_date,
       Count(DISTINCT(product)) AS num_sold,
       Group_concat(DISTINCT(product) SEPARATOR ',') AS products
FROM   activities
GROUP  BY sell_date
ORDER  BY sell_date
