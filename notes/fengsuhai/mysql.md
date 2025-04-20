以下是 Ubuntu 22.04 中安装、启动 MySQL，并设置 root 用户密码和创建数据库的详细步骤：
步骤 1：安装 MySQL

    更新系统包：

sudo apt update
sudo apt upgrade -y

安装 MySQL 服务器：

sudo apt install mysql-server -y

检查 MySQL 服务状态：

    sudo systemctl status mysql

    如果显示 active (running)，说明 MySQL 服务已经启动。

步骤 2：启动和启用 MySQL 服务

确保 MySQL 服务在开机时自动启动：

sudo systemctl enable mysql

启动 MySQL 服务（如果未运行）：

sudo systemctl start mysql

步骤 3：设置 root 用户密码

默认情况下，MySQL 安装时会使用 auth_socket 插件认证 root 用户，你需要切换为密码认证：

    登录 MySQL：

sudo mysql

切换到 mysql 数据库：

USE mysql;

修改 root 用户认证方式为密码认证，并设置密码 your_password：

ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'your_password';

刷新权限：

FLUSH PRIVILEGES;

退出 MySQL：

    EXIT;

步骤 4：创建数据库 o2oa

    登录 MySQL 使用刚设置的 root 用户和密码：

mysql -u root -p

输入密码 your_password。

创建数据库：

CREATE DATABASE o2oa;

确认数据库创建：

SHOW DATABASES;

应该可以看到 o2oa 数据库。

退出 MySQL：

    EXIT;

步骤 5：测试连接

    测试登录 MySQL：

mysql -u root -p

输入密码 your_password。

使用新创建的数据库：

    USE o2oa;
    SHOW TABLES;

补充：配置 MySQL 远程访问（可选）

如果你需要允许远程访问 root 用户：

    修改 MySQL 配置文件：

sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf

将 bind-address = 127.0.0.1 改为 bind-address = 0.0.0.0，然后保存退出。

在 MySQL 中为 root 设置远程访问权限：

GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'your_password';
FLUSH PRIVILEGES;

重启 MySQL 服务：

    sudo systemctl restart mysql

完成以上步骤后，你的 MySQL 安装已经成功，root 用户密码已设置为 your_password，并创建了数据库 o2oa。