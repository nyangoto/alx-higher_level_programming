-- lists all records in the table 'second_table' in the database hbtn_0c_0
-- that have a score >= 10
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
