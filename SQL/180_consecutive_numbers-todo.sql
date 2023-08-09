-- Not Solved yet
-- {"headers": {"Logs": ["id", "num"]}, "rows": {"Logs": [[1, 1], [2, 2], [3, 1], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [9, 3], [10, 3], [11, 4], [12, 3]]}}
WITH rank_table AS (
SELECT
    num,
    id,
    ROW_NUMBER() OVER(
        PARTITION BY num
        ORDER BY id
    ) AS rank
FROM
    Logs
)

SELECT
    num AS "ConsecutiveNums"
FROM
(
    SELECT
        num,
        SUM(id)
    FROM
        rank_table
    WHERE rank <= 3
    GROUP BY num
    HAVING MOD(SUM(id), 3) = 0
)
