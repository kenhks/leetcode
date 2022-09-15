-- Solution 1: MySQL
SELECT e.name AS employee
FROM employee e
LEFT JOIN employee e2 on e.managerId = e2.id
WHERE e.salary > e2.salary
