-- Solution 1: MySQL, Rank
SELECT t.Department, t.Employee, t.Salary
FROM (
    SELECT
        d.name AS 'Department',
        e.name AS 'Employee', 
        e.salary AS 'Salary', 
        DENSE_RANK() OVER (PARTITION BY D.id ORDER BY E.salary DESC) AS 'rank'
    FROM employee e
    LEFT JOIN department d ON e.departmentId = d.id
) t
WHERE t.rank <= 3