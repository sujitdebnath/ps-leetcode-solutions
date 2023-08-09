-- Solution 1
SELECT
    email AS "Email"
From
    (
        SELECT
            email,
            COUNT(*)
        FROM
            Person
        GROUP BY email
        HAVING COUNT(*) > 1
    );


-- Solution 2
SELECT
    email AS "Email"
From
    (
        SELECT
            email,
            COUNT(*) AS occurrence
        FROM
            Person
        GROUP BY email
    )
WHERE occurrence > 1;