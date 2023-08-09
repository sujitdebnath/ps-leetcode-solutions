CREATE FUNCTION getNthHighestSalary(
    N IN NUMBER)
RETURN NUMBER
IS
    result NUMBER;
BEGIN
    SELECT DISTINCT salary INTO result
    FROM
        (
            SELECT
                salary,
                DENSE_RANK() OVER(
                    ORDER BY salary DESC
                ) AS rank
            FROM
                Employee
        )
    WHERE rank = N;
    
    RETURN result;
END;