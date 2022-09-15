-- Solution 1: MySQL, Rank
SELECT t.Department, t.Employee, t.Salary
FROM (
    SELECT
        d.name AS 'Department',
        e.name AS 'Employee', 
        e.salary AS 'Salary', 
        RANK() OVER (PARTITION BY D.id ORDER BY E.salary DESC) AS 'rank'
    FROM employee e
    LEFT JOIN department d ON e.departmentId = d.id
) t
WHERE t.rank =1

-- Solution 2: MySQl, filter by department max
SELECT
    Department.name AS 'Department',
    Employee.name AS 'Employee',
    Salary
FROM
    Employee
        JOIN
    Department ON Employee.DepartmentId = Department.Id
WHERE
    (Employee.DepartmentId , Salary) IN
    (   SELECT
            DepartmentId, MAX(Salary)
        FROM
            Employee
        GROUP BY DepartmentId
    )
