```shell
sudo apt update
sudo apt install xvfb x11vnc fluxbox gnome-session

nano start-virtual-desktop.sh
```

```sh
#!/bin/bash
# A script to start a virtual X session with GNOME

# Choose a display number for the virtual display (e.g., :99)
DISPLAY_NUM=:99

# Start Xvfb on the chosen display number
Xvfb $DISPLAY_NUM -screen 0 1920x1080x24 &

# Export the DISPLAY environment variable so applications use the virtual display
export DISPLAY=$DISPLAY_NUM

# Wait a moment for Xvfb to start
sleep 2

# Start a GNOME session in the virtual display
gnome-session &

# You can also start a VNC server for debugging (optional)
# x11vnc -display $DISPLAY_NUM -forever -viewonly -rfbport 5900 &

echo "Virtual GNOME desktop started on display $DISPLAY_NUM."
```

```shell
chmod +x start-virtual-desktop.sh
./start-virtual-desktop.sh
sudo pkill -f rustdesk
export DISPLAY=:99
sudo /usr/bin/rustdesk --service
sudo -u bawuyinguo DISPLAY=:99 /usr/bin/rustdesk --service
sudo /usr/share/rustdesk/rustdesk --server
```


## mcsm启动命令：
```
sudo -u bawuyinguo DISPLAY=:99 /usr/bin/rustdesk --service
```