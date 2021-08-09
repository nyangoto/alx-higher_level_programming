-- Create database 'hbtn_0d_2' and user 'user_0d_2'
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

/* Create user 'user_0d_2' */
CREATE USER IF NOT EXISTS user_0d_2@localhost;

/* Set new user's password */
SET PASSWORD FOR user_0d_2@localhost = 'user_0d_2_pwd';

/* Grant new user SELECT privilege */
GRANT SELECT
	ON hbtn_0d_2.*
	TO user_0d_2@localhost;
