CREATE DATABASE IF NOT EXISTS solfacil;
SET user_exists = (SELECT COUNT(*) FROM mysql.user WHERE user = 'admin' AND host = '%');
IF user_exists = 0 THEN
    CREATE USER 'admin'@'%' IDENTIFIED BY 'admin';
    GRANT ALL PRIVILEGES ON solfacil.* TO 'admin'@'%';
END IF;
FLUSH PRIVILEGES;