-- Solution 1
SELECT
    d.name AS "Department",
    e.name AS "Employee",
    e.salary AS "Salary"
FROM Employee e
LEFT JOIN Department d ON e.departmentId = d.id
LEFT JOIN (
        SELECT
            departmentId,
            MAX(salary) AS max_salary
        FROM
            Employee
        GROUP BY departmentId
) m ON e.departmentId = m.departmentId
WHERE e.salary = m.max_salary;


-- Solution 2
SELECT
    d.name AS "Department",
    e.name AS "Employee",
    e.salary AS "Salary"
FROM
    Employee e,
    Department d,
    (
        SELECT
            departmentId,
            MAX(salary) AS max_salary
        FROM
            Employee
        GROUP BY departmentId
    ) m
WHERE e.departmentId = d.id
      AND e.departmentId = m.departmentId
      AND e.salary = m.max_salary;