-- Displays the max temperature of each state from the temperatures table
SELECT state,
	MAX(value) AS "max_temp"
	FROM temperatures
	GROUP BY state
	ORDER BY state;
