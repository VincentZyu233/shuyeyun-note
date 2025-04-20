你的第一个问题是，fallocate 报错提示 No such file or directory，说明目标目录 /mnt/data/ 不存在。以下是可能的解决方案和完整步骤：
问题分析

    /mnt/data/ 路径不存在，因此无法创建 swapfile 文件。
    在创建交换文件前，确保目标目录已经存在且可写。

解决方案

按照以下步骤操作，确保能够成功创建交换空间：

    创建目录（如有需要） 如果 /mnt/data 目录不存在，创建它：

mkdir -p /mnt/data

分配交换文件 使用 fallocate 创建 10GB 的交换文件：

fallocate -l 10G /mnt/data/swapfile

设置权限 确保交换文件的权限是 600，以防止其他用户访问：

chmod 600 /mnt/data/swapfile

创建交换空间 初始化交换文件：

mkswap /mnt/data/swapfile

启用交换空间 将其激活为系统的交换空间：

swapon /mnt/data/swapfile

验证交换空间 使用以下命令确认交换空间已启用：

swapon --show
free -h

永久启用交换空间 编辑 /etc/fstab，添加以下行：

/mnt/data/swapfile none swap sw 0 0

这样，在系统重启后，交换空间仍会被自动启用。
sudo sysctl vm.swappiness=100  
sudo sysctl vm.swappiness=50
sudo sysctl vm.swappiness=10

# 设置为10，减少交换空间的使用


## 永久设置swappiness：
2. 永久设置 swappiness 为 0

编辑 /etc/sysctl.conf 文件：

sudo nano /etc/sysctl.conf

添加或修改以下行：

vm.swappiness=0

保存并退出（按 Ctrl+O 然后 Ctrl+X）。

使设置立即生效：

sudo sysctl -p

## 实操记录：

```bash
root@ser4500530465:/# qwq
Command 'qwq' not found, did you mean:
  command 'qrq' from snap qrq (0.3.1)
  command 'qrq' from deb qrq (0.3.5-1)
  command 'qwo' from deb qwo (0.5-3)
See 'snap info <snapname>' for additional versions.
root@ser4500530465:/# swapon --show
NAME               TYPE SIZE USED PRIO
/mnt/data/swapfile file  34G   2M   -2
root@ser4500530465:/# sudo swapoff /mnt/data/swapfile
root@ser4500530465:/# swapon --show
root@ser4500530465:/# sudo rm /mnt/data/swapfile
root@ser4500530465:/# sudo fallocate -l 4G /mnt/data/swapfile
root@ser4500530465:/# sudo chmod 600 /mnt/data/swapfile
root@ser4500530465:/# sudo mkswap /mnt/data/swapfile
Setting up swapspace version 1, size = 4 GiB (4294963200 bytes)
no label, UUID=27aca6c4-da06-4464-8959-e347e8cf9542
root@ser4500530465:/# sudo swapon /mnt/data/swapfile
root@ser4500530465:/# swapon --show
NAME               TYPE SIZE USED PRIO
/mnt/data/swapfile file   4G   0B   -2
root@ser4500530465:/# sudo nano /etc/fstab
root@ser4500530465:/# sudo sysctl vm.swappiness=5
vm.swappiness = 5
root@ser4500530465:/# swapon --show
cat /proc/sys/vm/swappiness
NAME               TYPE SIZE USED PRIO
/mnt/data/swapfile file   4G   0B   -2
5
root@ser4500530465:/# 
```