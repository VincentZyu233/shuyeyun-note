screen -S nb
nb run
按下 Ctrl+A，然后 D，可以将会话分离，服务依然在后台运行。
screen -r nb


screen -ls
screen -S nb -X quit

screen -S <会话ID> -X quit

screen -d 4050657.nb

### screen
screen -S <name>
按下 Ctrl+A，然后 D，可以将会话分离，服务依然在后台运行。
screen -r <name>

screen -ls
screen -S <name> -X quit
screen -S <会话ID> -X quit


### 命名规范
napcat
nb
velocity
lobby
parkour
mix
bingo
ut

### 一键返回
screen -r napcat
screen -r nb
screen -r velocity
screen -r lobby
screen -r parkour
screen -r mix
screen -r bingo
screen -r ut