-- Solution 1
SELECT stock_name, 
    SUM(
        CASE 
            WHEN operation = 'BUY' THEN -price
            ELSE price
        END
    ) AS capital_gain_loss
FROM stocks
GROUP BY stock_name
