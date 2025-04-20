好的！那我们就用 Nginx 来提供资源包下载。下面是详细的 Nginx 配置步骤，确保你的 Minecraft 服务器可以稳定地提供资源包。
📌 Nginx 配置步骤
1️⃣ 安装 Nginx

如果你的服务器还没有 Nginx，先安装：

apt update && apt install nginx -y

安装完成后，Nginx 默认会自动启动，你可以用以下命令检查：

systemctl status nginx

如果没有运行，启动它：

systemctl start nginx

2️⃣ 复制资源包到 Nginx 目录

推荐把资源包放在 /var/www/html/resources/：

mkdir -p /var/www/html/resources
cp /mnt/vda1/SSoftwareFiles/minecraft/resources_dir/*.zip /var/www/html/resources/

然后检查文件：

ls -lh /var/www/html/resources/

确保资源包 都已复制。
3️⃣ 配置 Nginx

编辑 Nginx 配置文件：

nano /etc/nginx/sites-available/minecraft_resources

然后添加以下内容：

server {
    listen 80;
    server_name 103.150.11.254;  # 这里改成你的公网 IP 或域名

    location /resources/ {
        root /var/www/html/;
        autoindex on;  # 允许显示目录内容（可选）
    }
}

然后启用该站点：

ln -s /etc/nginx/sites-available/minecraft_resources /etc/nginx/sites-enabled/

检查配置是否正确：

nginx -t

如果没有报错，重启 Nginx：

systemctl restart nginx

4️⃣ 在 server.properties 里设置

resource-pack=http://103.150.11.254/resources/resources_random.zip

🚀 然后重启 Minecraft 服务器，测试客户端是否能正确下载资源包。
🎯 进阶：开启 HTTPS（推荐）

如果你有 域名，可以用 certbot 自动申请 HTTPS 证书：

apt install certbot python3-certbot-nginx -y
certbot --nginx -d 你的域名

然后改 server.properties：

resource-pack=https://你的域名/resources/resources_random.zip

这样资源包下载就是 HTTPS，更安全 😃
💡 常见问题
1️⃣ 客户端提示“无法下载资源包”

    试试在浏览器访问：

    http://103.150.11.254/resources/resources_random.zip

    如果可以访问但 Minecraft 不下载，可能是 server.properties 没配置对。

2️⃣ Nginx 启动失败

    检查是否有其他程序占用了 80 端口：

netstat -tulnp | grep :80

如果看到 apache2，那说明 Apache 可能占用了 80 端口：

    systemctl stop apache2
    systemctl disable apache2
    systemctl restart nginx

3️⃣ 资源包太大，下载失败

Minecraft 默认超时 60 秒，可以在 server.properties 里设置：

resource-pack-prompt=Downloading pack...
resource-pack-sha1=你的资源包 SHA1 值

获取 SHA1 值：

sha1sum /var/www/html/resources/resources_random.zip

