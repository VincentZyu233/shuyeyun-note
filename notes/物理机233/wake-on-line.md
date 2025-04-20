
zyu@zyu:~$ ip link show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: enp2s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP mode DEFAULT group default qlen 1000
    link/ether 44:8a:5b:9a:08:6b brd ff:ff:ff:ff:ff:ff
zyu@zyu:~$

sudo ethtool enp2s0

sudo ethtool -s enp2s0 wol g
