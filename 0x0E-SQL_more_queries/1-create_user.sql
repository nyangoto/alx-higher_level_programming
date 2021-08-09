-- Create a MySQL server user 'user_0d_1' whose password is 'user_0d_1_pwd'
CREATE USER IF NOT EXISTS user_0d_1@localhost;

/* SET password for new user */
SET PASSWORD FOR user_0d_1@localhost = 'user_0d_1_pwd';

/* Grant new user all privileges on the MySQL Server */
GRANT ALL PRIVILEGES
	ON *.*
	TO user_0d_1@localhost;

