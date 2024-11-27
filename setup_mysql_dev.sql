-- create database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- create user if it doesn't exist attatched with password
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- grant all privileges only on hbnb_dev_db
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- grant select privileges only on performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- push privileges
FLUSH PRIVILEGES;
