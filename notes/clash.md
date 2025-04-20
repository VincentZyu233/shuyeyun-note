gunzip clash.gz


curl -o config.yaml "https://mercedes1208.xn--3iq226gfdb94q.com/link/VwkSzWNCfOP7rR6x?clash=1"


chmod +x ./clash
./clash -d ./

export http_proxy=http://127.0.0.1:7890
export https_proxy=http://127.0.0.1:7890
export all_proxy=socks5://127.0.0.1:7891

curl -I https://www.youtube.com
curl -I https://github.com
curl -H "Authorization: Bot <token>" https://discord.com/api/v10/users/@me



https://github.com/eorendel/clash-dashboard

git clone https://github.com/eorendel/clash-dashboard.git 

修改配置文件config.yaml中相应字段为 external-ui: path/to/clash-dashboard