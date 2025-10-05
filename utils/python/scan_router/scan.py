import platform
import subprocess
import concurrent.futures
import socket

def get_local_ip():
    """
    获取本机局域网IP
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # 任意目标地址都行，用于确定出口IP
        s.connect(('8.8.8.8', 80))
        local_ip = s.getsockname()[0]
    except Exception:
        local_ip = '127.0.0.1'
    finally:
        s.close()
    return local_ip

def ping(ip):
    """
    对指定IP执行ping命令，看能否ping通
    """
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', '-w', '1000', ip]
    try:
        result = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return ip if result.returncode == 0 else None
    except Exception:
        return None

def main():
    local_ip = get_local_ip()
    print(f"[+] 本机IP地址: {local_ip}")
    
    # 自动推断网段
    net_prefix = '.'.join(local_ip.split('.')[:3])
    print(f"[+] 假定扫描网段: {net_prefix}.0/24")

    ips_to_scan = [f"{net_prefix}.{i}" for i in range(1, 255)]

    print("[*] 正在扫描局域网设备，请稍候...")
    active_ips = []

    # 多线程加速扫描
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        results = executor.map(ping, ips_to_scan)
        for res in results:
            if res:
                active_ips.append(res)

    print("\n[+] 扫描到的活动设备IP地址：")
    for ip in active_ips:
        print(f" - {ip}")

if __name__ == "__main__":
    main()
