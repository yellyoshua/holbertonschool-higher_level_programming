-- Lists all records that contain a name
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;