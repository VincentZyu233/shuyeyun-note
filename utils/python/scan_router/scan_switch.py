import nmap
import socket

def scan_with_nmap():
    # 获取本机IP
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        my_ip = s.getsockname()[0]
    finally:
        s.close()
        
    network = my_ip.rsplit('.', 1)[0] + '.0/24'
    print(f"开始使用 Nmap 扫描网络 {network}...")

    nm = nmap.PortScanner()
    nm.scan(hosts=network, arguments='-sn')  # -sn 表示只进行主机发现，不进行端口扫描

    devices = []
    for host in nm.all_hosts():
        if 'mac' in nm[host]['addresses']:
            device = {
                'ip': host,
                'mac': nm[host]['addresses']['mac']
            }
            devices.append(device)
    return devices

if __name__ == "__main__":
    devices_in_network = scan_with_nmap()
    
    if devices_in_network:
        print("\n找到以下设备：")
        print("-" * 30)
        for device in devices_in_network:
            print(f"IP: {device['ip']}\tMAC: {device['mac']}")
        print("-" * 30)
    else:
        print("\n未找到任何设备。")