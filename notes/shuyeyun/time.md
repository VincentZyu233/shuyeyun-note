## 调整系统时区
```bash
timedatectl
sudo timedatectl set-timezone Asia/Shanghai
sudo apt-get install ntp
sudo systemctl enable ntp
sudo systemctl start ntp
sudo ntpdate cn.pool.ntp.org
```

```bash
python3
```

```python
from datetime import datetime
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

```