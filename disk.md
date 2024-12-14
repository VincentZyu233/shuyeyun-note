### disk

```bash
lsblk
sudo mkdir /mnt/data
sudo mount /dev/vdb1 /mnt/data

sudo cp /etc/fstab /etc/fstab.backup
sudo vim /etc/fstab

```

/dev/vdb1    /mnt/data    ext4    defaults    0    0

```bash
sudo mount -a
```