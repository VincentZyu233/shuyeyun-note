### ubuntu 22.04 apt换源
```bash
sudo vim /etc/apt/sources.list
```

```
deb http://mirrors.aliyun.com/ubuntu/ jammy main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ jammy-updates main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ jammy-backports main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ jammy-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ jammy main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ jammy-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ jammy-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ jammy-security main restricted universe multiverse
```

## ubuntu 22.04 pip换源
```bash
sudo vim /etc/pip.conf
```

```
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple

[install]
trusted-host = pypi.tuna.tsinghua.edu.cn
```

```bash
pip config list
```

```bash
scp ./Lagrange.OneBot_linux-x64_net8.0_SelfContained.tar.gz root@103.150.11.254:/root/SSoftwareFiles/lagrange

scp ./white.png root@103.150.11.254:/root/SSoftwareFiles/nonebot2/qwq-bot/

sudo apt update
sudo apt install python3-pip
python3 -m pip install --user pipx
python3 -m pipx ensurepath
sudo apt install pipx
pipx install nb-cli

sudo apt update
sudo apt install libgl1-mesa-glx


```

## discord 对接
```bash
nb adapter install nonebot-adapter-discord
nb adapter uninstall nonebot-adapter-discord

```

安装websocket 的 driver， discord的adapter
DRIVER=~fastapi+~websockets+~httpx

curl -o config.yaml "http://124.222.64.172:61234/link/VwkSzWNCfOP7rR6x?clash=1"
gzip -d <gz-file-name>
chmod +x ./clash-linux-amd64-v3-v1.18.0

export http_proxy="socks5://127.0.0.1:1080"
export https_proxy="socks5://127.0.0.1:1080"
./clash-linux-amd64-v3-v1.18.0 -d .

export http_proxy=http://127.0.0.1:7890
export https_proxy=http://127.0.0.1:7890

ps aux | grep clash
netstat -tuln | grep 7890
lsof -i :7890

curl -I -x http://localhost:7890 https://discord.com/api/v10


curl https://www.google.com
curl -I https://www.google.com

curl https://www.baidu.com
curl -I https://discord.com/api/v10
curl -I -x http://127.0.0.1:7890 https://discord.com/api/v10



## v2ray 配置
curl -o v2ray_config_base64.txt  "http://124.222.64.172:61234/link/VwkSzWNCfOP7rR6x?sub=5"
cat v2ray_config_base64.txt | base64 --decode > v2ray_config_link.txt


sudo cp v2ray /usr/local/bin
sudo cp v2ctl /usr/local/bin
export http_proxy="socks5://127.0.0.1:1080"
export https_proxy="socks5://127.0.0.1:1080"

v2ray -config ./config.json

curl https://www.google.com

head -n 10 ./config.json

sudo mv ./geosite.dat /usr/local/bin/
sudo mv ./geoip.dat /usr/local/bin/

## napcat
```bash
xvfb-run -a qq --no-sandbox 

sudo vim /opt/QQ/resources/app/app_launcher/napcat/config/webui.json

sudo find / -type f -name "*napcat*"

sudo lsof -i :8080
```

## nb plugins 

nb plugin install nonebot_plugin_analysis_bilibili
nb plugin install nonebot_plugin_charpic
nb plugin install nonebot_plugin_picmcstat
nb plugin install nonebot_plugin_nowtime
nb plugin install nonebot_plugin_picstatus
nb plugin install nonebot-plugin-easymarkdown



## 限制内存
ulimit -v 1048576
ulimit -v 2097152
ulimit -v 2222222
nb run

## 查看被占用端口 
```bash
lsof -i 8080
sudo kill -9 <pid>
```