```bash
sudo apt update
sudo apt install lxqt

sudo apt install tightvncserver
vncserver
nano ~/.vnc/xstartup

```

#!/bin/sh

xrdb "$HOME/.Xresources"
xsetroot -solid grey

# Start LXQt
startlxqt &


```bash
chmod +x ~/.vnc/xstartup
vncserver -kill :1
vncserver :1
ssh -L 5901:localhost:5901 root@103.150.11.254

```

ps aux | grep Xtightvnc

vncserver -kill :1
vncserver :1

cat ~/.vnc/*.log

sudo ufw status
sudo ufw allow 5901

ping 103.150.11.254

startx

sudo apt install xfonts-75dpi xfonts-100dpi
touch ~/.Xresources
