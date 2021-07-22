-- Display the average temperature by city ordered by temperature (dec)
-- from the 'temperatures' table in hbtn_0c_0 database
SELECT city,
AVG(value) AS 'avg_temp'
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
