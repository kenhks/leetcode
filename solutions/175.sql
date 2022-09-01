-- Solution 1
SELECT
  firstname,
  lastname,
  city,
  state
FROM
  person
  LEFT JOIN address ON address.personid = person.personId
