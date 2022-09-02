-- Solution 1: EXCEPT/MINUS Oracle
SELECT s.name
FROM salesperson s
MINUS
SELECT s.name
FROM salesperson s 
INNER JOIN orders o ON o.sales_id = s.sales_id
INNER JOIN company c ON o.com_id = c.com_id AND c.name = 'RED'

-- Solution 2: NOT IN
SELECT
    s.name
FROM
    salesperson s
WHERE
    s.sales_id NOT IN (
        SELECT
            o.sales_id
        FROM
            orders o
                LEFT JOIN
            company c ON o.com_id = c.com_id
        WHERE
            c.name = 'RED'
        )