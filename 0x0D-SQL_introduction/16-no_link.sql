-- This script lists the name and score of all records of `second_table`
SELECT score, name
FROM second_table
WHERE name != ''
ORDER BY score DESC;
