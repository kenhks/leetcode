-- Solution
SELECT u.name, SUM(amount) AS balance
FROM users AS u
LEFT JOIN transactions AS t ON u.account = t.account
GROUP BY u.account, u.name
HAVING balance >= 10000
