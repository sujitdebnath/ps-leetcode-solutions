-- Solution 1
SELECT
    c.name AS "Customers"
FROM Customers c
LEFT JOIN Orders o ON c.id = o.customerId
WHERE o.customerId IS NULL;


-- Solution 2
SELECT
    name AS "Customers"
FROM
    (
        SELECT
            c.name,
            o.customerId
        FROM Customers c
        LEFT JOIN Orders o ON c.id = o.customerId
    )
WHERE customerId IS NULL;