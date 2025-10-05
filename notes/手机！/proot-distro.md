在 Termux 中使用 Proot-Distro 安装的 Ubuntu 22.04 系统，可以通过以下步骤进入：
步骤一：确保已安装 Proot-Distro

如果您还没有安装 proot-distro，首先需要通过 Termux 安装它。打开 Termux 应用程序并执行以下命令来安装 proot-distro：

shell
深色版本

pkg install proot-distro

步骤二：安装 Ubuntu 发行版

如果尚未安装 Ubuntu 22.04，请通过 proot-distro 来安装。这可以通过下面的命令完成：

shell
深色版本

proot-distro install ubuntu-22.04

此命令会下载并设置一个基于 Ubuntu 22.04 的 Proot 环境。根据您的网络连接速度，这可能需要一些时间。
步骤三：启动或进入 Ubuntu

一旦安装完成，您可以随时通过以下命令启动并进入 Ubuntu 环境：

shell
深色版本

proot-distro login ubuntu-22.04

这个命令将会启动您安装的 Ubuntu 发行版，并提供一个登录提示符。首次启动时，您可能会被要求设置 root 密码和其他初始配置信息。
步骤四：使用 Ubuntu

成功登录后，您将处于 Ubuntu 22.04 的环境中，可以像平常一样使用命令行工具和安装软件包。例如，更新系统和安装新软件包可以使用如下命令：

shell
深色版本

apt update && apt upgrade -y
apt install <package-name>


# ssh
https://github.com/termux/proot-distro/issues/219
```bash
/usr/sbin/sshd
```