-- Lists all records of the table 'second_table" of the database hbtn_0c_0
-- where name is not empty
-- should be listed in descending order
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
