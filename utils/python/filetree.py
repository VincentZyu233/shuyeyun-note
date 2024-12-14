"""
python filetree.py

E:\GGames\Minecraft\shuyeyun\mc-server\plugins\MySpigotPluginsProjects\qwq-spigot-plugin\qwq-spigot-plugin
"""
import os
from pathlib import Path

def tree(directory, prefix=""):
    """递归地打印目录树"""
    # 获取当前目录下的所有文件和子目录
    entries = list(directory.iterdir())
    
    # 如果当前目录为空，则直接返回
    if not entries:
        print(f"{prefix}└── {directory.name}/")
        return
    
    # 打印当前目录
    print(f"{prefix}├── {directory.name}/")
    
    # 递归处理每个条目
    for i, entry in enumerate(entries):
        is_last = i == len(entries) - 1
        new_prefix = f"{prefix}│   " if not is_last else f"{prefix}    "
        
        if entry.is_dir():
            tree(entry, new_prefix)
        else:
            print(f"{new_prefix}├── {entry.name}" if not is_last else f"{new_prefix}└── {entry.name}")

if __name__ == "__main__":
    # 输入路径
    path = input("请输入目录路径: ")
    
    # 将输入的路径转换为 Path 对象
    directory = Path(path)
    
    # 检查路径是否存在且是目录
    if directory.exists() and directory.is_dir():
        # 打印根目录
        print(f"/{directory.name}")
        # 生成目录树
        tree(directory, "")
    else:
        print("无效的目录路径，请检查后重试。")