. 解决方法
方法一：降级 Python 版本

尝试使用一个更稳定的 Python 版本，比如 Python 3.10 或 3.9，这些版本已经被广泛测试，并且大多数包都已经为它们进行了优化。

你可以通过 pyenv 或者直接安装特定版本的 Python 来实现这一点：

bash
深色版本

# 使用 pyenv 安装 Python 3.10
curl https://pyenv.run | bash
exec $SHELL
pyenv install 3.10.12
pyenv global 3.10.12

# 确认安装成功
python --version

然后重新创建虚拟环境并安装 nb-cli 和其他依赖项：

bash
深色版本

pipx uninstall nb-cli
pipx install nb-cli