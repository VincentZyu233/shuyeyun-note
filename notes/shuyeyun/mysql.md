sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf
bind-address = 0.0.0.0
sudo systemctl restart mysql

sudo mysql -u root -p
CREATE USER 'vincentzyu'@'%' IDENTIFIED BY 'diding2014';
GRANT ALL PRIVILEGES ON *.* TO 'vincentzyu'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;
GRANT ALL PRIVILEGES ON *.* TO 'vincentzyu'@'%' IDENTIFIED BY 'diding2014' WITH GRANT OPTION;
FLUSH PRIVILEGES;



-----

shuyeyun:

apt install mysql-server
service mysql status
mysql -u root -p


CREATE USER 'zyu'@'localhost' IDENTIFIED BY '6';
GRANT ALL PRIVILEGES ON qwq.* TO 'zyu'@'localhost';
FLUSH PRIVILEGES;

CREATE DATABASE qwq;