以下是 BungeeCord 配置文件 config.yml 的各个配置项说明：
基础配置

    server_connect_timeout: 5000
        客户端连接到后端服务器的超时时间（以毫秒为单位）。超过这个时间后，连接会中断。

    enforce_secure_profile: false
        是否强制玩家启用 Mojang 的安全验证系统。在多数情况下保留为 false。

    remote_ping_cache: -1
        控制远程 ping 数据的缓存时间。-1 表示禁用缓存。

    forge_support: false
        是否启用对 Forge 模组的支持。启用后，BungeeCord 会正确处理带有模组的连接。

    player_limit: -1
        最大玩家数量，-1 表示没有限制。

权限相关

    permissions
        配置权限组及其对应的权限指令：
            default：普通玩家的默认权限。
            admin：管理员权限，例如服务器管理、踢人、发送公告等。

服务器设置

    timeout: 30000
        服务器连接的超时时间（以毫秒为单位）。连接超过此时间无响应会被中断。

    log_commands: false
        是否记录玩家执行的命令到日志中。

    network_compression_threshold: 256
        数据包压缩阈值。低于此字节大小的数据包不会被压缩。

    online_mode: true
        是否启用 Mojang 验证。true 表示玩家需要正版账号，false 则允许离线模式玩家。

    disabled_commands
        禁用的指令列表（如需要，可以在列表中添加指令）。

服务器实例定义

    servers
        定义可连接的后端服务器。
        lobby：一个示例服务器配置。
            motd：服务器的 MOTD（玩家列表显示的消息）。
            address：服务器的 IP 地址和端口。
            restricted：是否限制普通玩家访问。

监听器配置

    listeners
        BungeeCord 代理监听的设置，支持多个监听器。
        query_port: 25577：启用查询协议时的监听端口。
        motd：代理显示的 MOTD。
        tab_list：控制 Tab 列表的显示模式，可为 GLOBAL_PING、GLOBAL 或 SERVER。
        query_enabled：是否启用查询协议。
        proxy_protocol：是否启用代理协议。
        forced_hosts：强制主机规则，用于根据输入的地址选择服务器。
        ping_passthrough：是否将后端服务器的 ping 信息传递给客户端。
        priorities：连接的优先服务器列表（按顺序）。
        bind_local_address：是否绑定到本地地址。
        host：代理绑定的主机和端口。
        max_players：最大玩家数限制。
        tab_size：Tab 列表的最大显示人数。
        force_default_server：是否强制玩家每次连接到默认服务器。

转发和安全设置

    ip_forward: false
        是否启用 IP 转发。启用后需要在后端服务器中配合 bungeecord: true。

    remote_ping_timeout: 5000
        远程 ping 请求的超时时间（以毫秒为单位）。

    reject_transfers: false
        是否拒绝玩家的服务器转移请求。

    prevent_proxy_connections: false
        是否阻止非代理连接直接访问后端服务器。

分组和性能设置

    groups
        定义玩家与权限组的关联。

    connection_throttle: 4000
        控制连接速率，防止短时间内的过多连接。

    stats
        匿名统计信息的 UUID。

    connection_throttle_limit: 3
        限制短时间内允许的最大连接数。

    log_pings: true
        是否记录 ping 信息到日志。

此配置文件为 BungeeCord 的基本设置，用户可根据自己的需求进行调整。如需更详细的说明，可以查看官方文档或社区资源​
SpigotMC - High Performance Minecraft
​
SpigotMC - High Performance Minecraft
。