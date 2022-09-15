-- Solution 1: MySQL
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
     SELECT salary 
     FROM (
        SELECT DISTINCT salary,
        DENSE_RANK() OVER (ORDER BY salary DESC) AS 'rank'
          FROM employee
       ) AS t
      WHERE t.rank=N
  );
END
