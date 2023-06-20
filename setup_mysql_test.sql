-- prepare MySQL server for AirBnB
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVELEGES ON 'hbnb_test_db'.* TO 'hbnb_test';
GRANT SELECT ON 'performance_schema'.* TO 'hbnb_test';
FLUSH PRIVELEGES;
