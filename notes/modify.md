## bungeecord config
player_limit: -1 -> 2024


servers
        定义可连接的后端服务器。
        lobby：一个示例服务器配置。
            motd：服务器的 MOTD（玩家列表显示的消息）。
            address：服务器的 IP 地址和端口。 -> localhost:23333
            restricted：是否限制普通玩家访问。


## spigot.yml in paper dir:
settings:
  # bungeecord: false
  bungeecord: true