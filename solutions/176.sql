-- Solution 1
SELECT  MAX(salary) AS SecondHighestSalary
FROM    Employee
WHERE   salary NOT IN (
                        SELECT  MAX(salary)
                        FROM    Employee
                      )
;
-- Solution 2
SELECT DISTINCT
    Salary AS SecondHighestSalary
FROM
    Employee
ORDER BY Salary DESC
LIMIT 1 OFFSET 1
