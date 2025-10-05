from scapy.all import ARP, Ether, srp
import sys
import socket

# 该脚本需要以管理员权限运行，以发送和接收网络数据包。
# 如果你使用的是Windows，请在管理员模式的命令提示符或PowerShell中运行。
# 如果你使用的是Linux/macOS，请使用 sudo python scan_network.py。

def get_local_ip():
    """
    获取本地设备的IP地址，以便确定所在的子网。
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception:
        return None

def scan_network(target_ip_range):
    """
    扫描指定IP范围内的所有设备，并打印它们的IP和MAC地址。
    使用ARP请求来发现设备。
    """
    print(f"正在扫描网络: {target_ip_range}")

    # 创建一个ARP请求数据包，询问目标IP
    arp_request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=target_ip_range)

    # srp()发送和接收数据包，verbose=False关闭输出，timeout设置超时时间
    answered, unanswered = srp(arp_request, timeout=1, verbose=False)

    print("-" * 50)
    print(" IP地址\t\t\tMAC地址")
    print("-" * 50)
    
    # 遍历已响应的设备
    if not answered:
        print("未找到任何设备。请确保你所在的网络和目标网段一致。")
    
    for sent, received in answered:
        ip = received.psrc
        mac = received.hwsrc
        print(f" {ip}\t\t{mac}")
    
    print("-" * 50)

def get_mac_address(ip_address):
    """
    通过ARP请求获取指定IP地址的MAC地址。
    """
    print(f"正在尝试获取 {ip_address} 的MAC地址...")
    try:
        arp_request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip_address)
        answered, _ = srp(arp_request, timeout=1, verbose=False)
        if answered:
            return answered[0][1].hwsrc
        else:
            return None
    except Exception as e:
        print(f"获取MAC地址失败: {e}")
        return None

if __name__ == "__main__":
    local_ip = get_local_ip()
    if not local_ip:
        print("无法自动获取本地IP地址。请手动输入IP范围。")
        default_ip_range = ""
    else:
        ip_parts = local_ip.split('.')
        default_ip_range = f"{ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}.0/24"

    while True:
        print("\n请选择一个操作:")
        print(f"1. 扫描当前网络 ({default_ip_range if local_ip else '需要手动输入'})")
        print("2. 扫描其他网络 (例如光猫所在网段)")
        print("3. 通过IP获取MAC地址")
        print("4. 退出")
        choice = input("你的选择: ")
        
        if choice == '1':
            if default_ip_range:
                scan_network(default_ip_range)
            else:
                print("本地IP未获取到，请选择其他选项手动输入。")
        elif choice == '2':
            ip_range = input("请输入要扫描的IP范围 (例如: 192.168.1.0/24): ")
            if ip_range:
                scan_network(ip_range)
        elif choice == '3':
            ip = input("请输入要查询的IP地址: ")
            if ip:
                mac = get_mac_address(ip)
                if mac:
                    print(f"找到的MAC地址是: {mac}")
                else:
                    print(f"未找到 {ip} 的MAC地址。")
        elif choice == '4':
            print("程序退出。")
            break
        else:
            print("无效的选择，请重新输入。")
