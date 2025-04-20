【无正版验证】
巨大略群的游乐园 神秘小服服：
    [Java 1.21.3 纯原版可进]
    (推荐版本是1.21.3, 其他的高版本也是可以的，但是某些子服资源包会有问题)
    (进服以后先/reg注册或者/l登录，然后右键指南针菜单 或者 /server指令 可以切换子服)
    地址：mc.vincentzyu233.xyz

    [基岩版 最新版本可进]
    地址：mc.vincentzyu233.xyz
    端口：19132

璃子和略的跑酷《寄跑天堂》：
    [基岩版 内地]
    地址：mc.vincentzyu233.xyz
    端口：22222

    [基岩版 海外]
    地址：uscc.mc.vincentzyu233.xyz
    端口：22047

    [Java版移植]
    (指令部分在重新建设中，基岩存档转JAVA指令全部失效)
    (进服以后先/reg注册或者/l登录，然后右键指南针菜单 或者 /server指令 可以切换子服)
    地址：mc.vincentzyu233.xyz

跑酷计分板：
    [复制到浏览器打开]
    http://qsfrontend.vincentzyu233.xyz/
    [QQ小程序]
    本群群应用 或者 直接首页搜索"跑酷服务器计分板"


一些子服资源包手动下载链接：
    [复制到浏览器打开]
    mc.vincentzyu233.xyz:55555

这里可以下载一些mc客户端资源：
    [复制到浏览器打开]
    (安卓/Windows 的 Java/基岩)
    mc.vincentzyu233.xyz:50405



docker run -it \
    --device /dev/kvm \
    -p 50922:10022 \
    -e "DISPLAY=${DISPLAY:-:0.0}" \
    -v /mnt/wslg/.X11-unix:/tmp/.X11-unix \
    -e GENERATE_UNIQUE=true \
    -e MASTER_PLIST_URL='https://raw.githubusercontent.com/sickcodes/osx-serial-generator/master/config-custom.plist' \
    registry.cn-hangzhou.aliyuncs.com/shrimp-images/docker-osx:ventura

# docker build -t docker-osx .


    -e HTTP_PROXY="http://localhost:7890" \
    -e HTTPS_PROXY="http://localhost:7890" \
    -e NO_PROXY="localhost,127.0.0.1" \
    
docker run -it \
    --device /dev/kvm \
    -p 50922:10022 \
    -e "DISPLAY=${DISPLAY:-:0.0}" \
    -v /mnt/wslg/.X11-unix:/tmp/.X11-unix \
    -e GENERATE_UNIQUE=true \
    -e MASTER_PLIST_URL='https://raw.githubusercontent.com/sickcodes/osx-serial-generator/master/config-custom.plist' \
    sickcodes/docker-osx:ventura


sudo docker run -it \
    --device /dev/kvm \
    -p 50922:10022 \
    -e "DISPLAY=${DISPLAY:-:0.0}" \
    -v /mnt/wslg/.X11-unix:/tmp/.X11-unix \
    -e GENERATE_UNIQUE=true \
    -e MASTER_PLIST_URL='https://gitee.com/lblk/osx-serial-generator/blob/master/config-custom.plist' \
    registry.cn-hangzhou.aliyuncs.com/shrimp-images/docker-osx:ventura

sudo docker run -it --device /dev/kvm -p 50922:10022 -e "DISPLAY=${DISPLAY:-:0.0}"  -v /mnt/wslg/.X11-unix:/tmp/.X11-unix -e GENERATE_UNIQUE=true -e MASTER_PLIST_URL='https://gitee.com/lblk/osx-serial-generator/blob/master/config-custom.plist' registry.cn-hangzhou.aliyuncs.com/shrimp-images/docker-osx:ventura



## 为什么ios禁止了jit？

## 为什么在ios上玩Minecraft java version 必须开启jit？ 为什么其他ios上的虚拟机 也要jit？

## jit对于Minecraft java在ios上运行 有什么优化吗

# ChatGPT 说：


iOS 禁止 JIT（即时编译，Just-In-Time Compilation）的主要原因是出于 安全性和稳定性 的考虑。JIT 编译允许在运行时动态生成和执行代码，这样做虽然可以提高程序的性能，但也带来了潜在的风险，比如：

    安全性：JIT 编译器可能会被滥用，攻击者可以利用它生成恶意代码，突破沙盒限制。
    系统稳定性：iOS 的沙盒环境要求应用程序运行在严格的安全边界内，而 JIT 编译可能会绕过一些安全限制，影响系统稳定性。
    系统控制：Apple 一直强调控制应用和资源的执行，以确保设备的性能、兼容性和更新的顺利进行。JIT 编译则可能破坏这种控制，尤其是在未经过验证的情况下动态执行代码。

为什么 Minecraft Java 版本需要开启 JIT

Minecraft Java 版（尤其是在像 iOS 这样的非原生平台上）需要 JIT 编译来提高运行性能。由于 Java 本身是一种基于虚拟机的语言，Java 字节码需要在运行时通过 JIT 编译器转化为机器码才能执行。没有 JIT，游戏的运行速度会大幅下降，因为 Java 代码会被逐条解释执行，而不是一次性编译成优化后的机器码。

在 iOS 上，Minecraft Java 版本并非原生运行，而是通过一些虚拟化或模拟技术来实现。因此，为了保持游戏的流畅度和性能，必须依赖 JIT 来提高代码执行效率。没有 JIT，Minecraft 的复杂计算和图形渲染会变得非常缓慢。
为什么其他 iOS 上的虚拟机也需要 JIT？

许多虚拟机（例如运行 Java 或其他语言的虚拟机）在 iOS 上也需要 JIT 来获得足够的执行性能。没有 JIT，这些虚拟机只能通过 解释执行 来运行代码，这样会极大地影响性能。因此，JIT 对于那些需要高性能的应用（如 Minecraft）是至关重要的，特别是在资源有限的设备（如 iOS 设备）上。
JIT 对于 Minecraft Java 在 iOS 上的优化

JIT 对 Minecraft Java 在 iOS 上的优化作用可以从几个方面来看：

    性能提升：JIT 可以动态优化代码，针对设备的具体架构生成高效的机器码，显著提高运行时性能，特别是对于复杂的计算和图形处理。
    内存优化：JIT 可以按需编译，只编译实际运行的代码段，避免无用代码占用内存。
    减少延迟：JIT 编译减少了解释执行时的延迟，提升了应用的响应速度，使得 Minecraft 的操作和交互更为流畅。

总的来说，JIT 对于在 iOS 上运行的 Minecraft Java 版本是一个必要的性能提升工具，能够让游戏在设备的限制下获得较好的表现。