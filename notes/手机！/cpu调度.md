## ubuntu22 如何强制cpu调度，让cpu的频率最小值是3.5GHz
在 Ubuntu 22.04 上强制调整 CPU 调度并设置最小频率为 3.5 GHz，首先需要确保你的 CPU 支持调整频率，并且系统已经安装了相关的工具来控制 CPU 的调度器。以下是设置方法：
1. 检查 CPU 频率调节器支持

首先，确认你的 CPU 支持调整频率。你可以使用以下命令来查看 CPU 支持的频率范围：

cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_available_frequencies

如果输出中包含 3.5 GHz，则说明可以设置为此频率。
2. 安装 cpufrequtils 工具

cpufrequtils 是一个用来控制 CPU 频率的工具，可以通过以下命令安装：

sudo apt update
sudo apt install cpufrequtils

3. 设置 CPU 最小频率为 3.5 GHz

使用 cpufreq-set 命令来设置 CPU 的最小频率。例如，要将最小频率设置为 3.5 GHz，可以运行以下命令：

sudo cpufreq-set -g performance  # 设置为性能模式
sudo cpufreq-set -d 3500000     # 设置最小频率为 3.5 GHz

在这个命令中，3500000 是 3.5 GHz 的频率（单位为 kHz），如果你希望设置为其他频率，只需将其修改为相应的值。
4. 确认设置

你可以使用以下命令来检查 CPU 当前的频率和调度器设置：

cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_cur_freq  # 当前频率
cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_min_freq  # 最小频率

5. 确保频率设置生效

你可以使用 cpufreq-info 命令查看当前 CPU 的所有频率设置：

cpufreq-info

6. 设置自动启动

为了让设置在每次启动时生效，可以将 cpufreq-set 命令添加到启动脚本中，或者在 rc.local 文件中设置。编辑 /etc/rc.local 文件（如果没有此文件，可以手动创建），并在文件中添加命令：

#!/bin/bash
cpufreq-set -g performance
cpufreq-set -d 3500000
exit 0

然后设置 rc.local 为可执行：

sudo chmod +x /etc/rc.local

注意事项：

    将 CPU 最小频率设置为 3.5 GHz 会导致更高的功耗，适合性能需求高的场景。
    如果 CPU 频率受硬件或系统限制，可能无法达到所设置的频率，请确保 CPU 可以稳定运行在这个频率下。



## 如何设置 统一设置最小评率是3.5GHz


ChatGPT 说：
ChatGPT

要统一设置所有 CPU 核心的最小频率为 3.5 GHz，你可以使用 cpupower 工具进行设置。请按照以下步骤操作：
步骤 1: 安装 cpupower 工具

如果你还没有安装 cpupower 工具，可以通过以下命令安装：

sudo apt update
sudo apt install linux-tools-common linux-tools-$(uname -r)

步骤 2: 设置最小频率

安装完 cpupower 后，使用以下命令设置最小频率为 3.5 GHz：

sudo cpupower frequency-set --min 3.5GHz

这个命令会将所有 CPU 核心的最小频率设置为 3.5 GHz。
步骤 3: 验证设置

可以通过以下命令验证最小频率设置是否生效：

cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_min_freq

你应该看到所有核心的最小频率都是 3.5 GHz。
注意事项

    如果 cpupower 工具提示无法设置频率，可能是因为你使用的 CPU 驱动（如 intel_pstate）不允许这种手动设置。
    如果要使设置生效并保持在系统重启后生效，你可以将相关命令添加到启动脚本中。

如果有其他问题，欢迎继续询问！