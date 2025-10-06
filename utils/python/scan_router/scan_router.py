# -*- coding: utf-8 -*-
from scapy.all import srp, Ether, ARP
import sys

# 您的路由器网关 IP
TARGET_IP = "192.168.31.1/24" 
# "/24" 表示扫描 192.168.31.1 到 192.168.31.254 整个网段

def scan_network(ip_range):
    """
    使用 ARP 协议扫描指定 IP 范围内的活动设备。
    
    ARP (Address Resolution Protocol) 扫描比传统的 Ping 扫描更快、更可靠，
    因为它直接在局域网内广播查询。
    """
    
    # 1. 构造以太网帧 / ARP 请求包
    # Ether(dst="ff:ff:ff:ff:ff:ff")：目标 MAC 地址为广播地址
    # ARP(pdst=ip_range)：ARP 目标 IP 范围
    arp_request = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip_range)
    
    print(f"[*] 正在扫描网段 {ip_range}...")
    
    # 2. 发送和接收数据包
    # timeout=1：等待响应的超时时间为 1 秒
    # verbose=False：关闭 Scapy 的详细输出
    answered, unanswered = srp(arp_request, timeout=1, verbose=False)
    
    devices = []
    
    # 3. 解析响应包
    for sent, received in answered:
        # received.hwsrc 是响应设备的 MAC 地址
        # received.psrc 是响应设备的 IP 地址
        devices.append({
            "IP": received.psrc,
            "MAC": received.hwsrc
        })

    return devices

if __name__ == "__main__":
    
    print("-" * 40)
    print("内网设备扫描器 (基于 Scapy)")
    print("-" * 40)
    
    # 执行扫描
    active_devices = scan_network(TARGET_IP)
    
    # 输出结果
    if active_devices:
        print("\n[+] 发现的内网活动设备:")
        print("=" * 30)
        print(f"{'IP 地址':<15}{'MAC 地址':<17}")
        print("=" * 30)
        for device in active_devices:
            # 格式化输出 IP 和 MAC 地址
            print(f"{device['IP']:<15}{device['MAC']:<17}")
        print("=" * 30)
        print(f"总共找到 {len(active_devices)} 个设备。")
    else:
        print("\n[-] 未发现活动设备。请检查网络连接和权限。")