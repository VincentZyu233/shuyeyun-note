import base64
import json
import yaml

def decode_vmess_link(vmess_link):
    # 解码 vmess 链接
    try:
        # 去掉前缀 vmess://
        base64_data = vmess_link[8:]
        # 解码 base64
        json_data = base64.b64decode(base64_data).decode('utf-8')
        return json.loads(json_data)
    except Exception as e:
        print(f"解码失败: {e}")
        return None

def generate_clash_config(vmess_data):
    # 从 vmess 数据生成 Clash 配置
    try:
        clash_config = {
            'proxies': [
                {
                    'name': 'V2Ray VMess',
                    'type': 'vmess',
                    'server': vmess_data.get('add'),
                    'port': vmess_data.get('port'),
                    'uuid': vmess_data.get('id'),
                    'alterId': vmess_data.get('aid'),
                    'cipher': 'auto',  # 默认 auto
                    'network': vmess_data.get('net', 'tcp'),  # 默认 tcp
                    'tls': False if vmess_data.get('tls') == 'none' else True,  # 根据 tls 设置
                    'wsPath': vmess_data.get('path', ''),
                    'wsHeaders': {'Host': vmess_data.get('host', '')}
                }
            ],
            'proxy-groups': [
                {
                    'name': 'Proxy',
                    'type': 'select',
                    'proxies': ['V2Ray VMess']
                }
            ],
            'rules': [
                {'DOMAIN-SUFFIX': 'google.com', 'target': 'PROXY'},
                {'DOMAIN-SUFFIX': 'facebook.com', 'target': 'PROXY'},
                {'GEOIP': 'CN', 'target': 'DIRECT'},
                {'MATCH': 'target': 'PROXY'}
            ]
        }
        return yaml.dump(clash_config, default_flow_style=False, allow_unicode=True)
    except Exception as e:
        print(f"生成 Clash 配置失败: {e}")
        return None

def main():
    # 输入 vmess 链接
    vmess_link = input("请输入 V2Ray vmess 链接: ")
    
    # 解码 vmess 链接
    vmess_data = decode_vmess_link(vmess_link)
    
    if vmess_data:
        # 生成 Clash 配置
        clash_config = generate_clash_config(vmess_data)
        
        if clash_config:
            print("\n生成的 Clash 配置文件:\n")
            print(clash_config)
            
            # 选择保存配置到文件
            save_to_file = input("\n是否将配置保存到文件？(y/n): ").strip().lower()
            if save_to_file == 'y':
                filename = input("请输入文件名 (如 clash_config.yaml): ").strip()
                with open(filename, 'w') as f:
                    f.write(clash_config)
                print(f"配置已保存到 {filename}")
            else:
                print("配置未保存。")
        else:
            print("生成 Clash 配置失败。")
    else:
        print("无法解析 V2Ray 链接。")

if __name__ == "__main__":
    main()
