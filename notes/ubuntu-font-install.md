在 Linux 系统中，你可以通过以下步骤将 OTF（OpenType 字体）文件安装到系统字体目录中。这样，你就可以在系统中的任何应用程序中使用这些字体，包括 LaTeX 和其他图形界面程序。
1. 复制字体文件到系统字体目录

首先，你需要将 OTF 文件复制到系统的字体目录。通常，这个目录是 /usr/share/fonts/ 或 ~/.local/share/fonts/。前者需要超级用户权限，后者则不需要。
使用系统范围的字体目录

如果你希望所有用户都能使用该字体，可以将其复制到 /usr/share/fonts/ 目录：

sh
深色版本

sudo cp /path/to/your/fontfile.otf /usr/share/fonts/

使用用户范围的字体目录

如果你只想为当前用户安装字体，可以将其复制到 ~/.local/share/fonts/ 目录：

sh
深色版本

mkdir -p ~/.local/share/fonts/
cp /path/to/your/fontfile.otf ~/.local/share/fonts/

2. 更新字体缓存

复制字体文件后，你需要更新字体缓存以使系统识别新安装的字体。这可以通过 fc-cache 命令完成。
对于系统范围的字体目录

如果你将字体文件复制到了 /usr/share/fonts/，请运行：

sh
深色版本

sudo fc-cache -fv

对于用户范围的字体目录

如果你将字体文件复制到了 ~/.local/share/fonts/，请运行：

sh
深色版本

fc-cache -fv

3. 验证字体是否安装成功

你可以使用 fc-list 命令来验证字体是否已经正确安装并被系统识别。例如，列出所有已安装的字体：

sh
深色版本

fc-list

或者，如果你只想查看特定字体是否安装成功，可以使用：

sh
深色版本

fc-list | grep "Source Han Serif SC"