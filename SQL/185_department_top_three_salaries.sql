-- Solution 1
WITH employee_rank AS (
    SELECT
        name,
        salary,
        departmentId,
        DENSE_RANK() OVER(
            PARTITION BY departmentId
            ORDER BY salary DESC
        ) AS ranking
    FROM Employee
)

SELECT
    d.name AS "Department",
    e.name AS "Employee",
    e.salary AS "Salary"
FROM employee_rank e
LEFT JOIN Department d ON e.departmentId = d.id
WHERE e.ranking <= 3;


-- Solution 2
SELECT
    d.name AS "Department",
    e.name AS "Employee",
    e.salary AS "Salary"
FROM
    (
        SELECT
            name,
            salary,
            departmentId,
            DENSE_RANK() OVER(
                PARTITION BY departmentId
                ORDER BY salary DESC
            ) AS ranking
        FROM Employee
    ) e
LEFT JOIN Department d ON e.departmentId = d.id
WHERE e.ranking <= 3;