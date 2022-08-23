-- Solution 1
SELECT name AS customers
FROM   customers
       LEFT JOIN orders
              ON orders.customerid = customers.id
WHERE  orders.id IS NULL
