-- Solution 1
SELECT *
FROM patients
WHERE conditions LIKE 'DIAB1%' or conditions LIKE '% DIAB1%'

-- Solution 2
SELECT *
FROM Patients
WHERE conditions REGEXP '\\bDIAB1'
