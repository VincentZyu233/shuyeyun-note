```bash
sudo apt install proxychains

nano /etc/proxychains.conf
```

```conf
[ProxyList]
socks5 127.0.0.1 7890
```

```bash
proxychains4 bash
curl -I https://www.google.com

proxychains4 curl -I https://www.google.com

proxychains screen -S foo
proxychains screen -S lagrange-ovo
proxychains screen -S koishi-ovo

proxychains screen -S fastapi-fuzzy-search-backend

curl -I https://www.google.com
```
