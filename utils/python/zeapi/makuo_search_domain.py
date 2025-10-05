import requests
import json
import concurrent.futures
from tqdm import tqdm

# --- Configuration ---
# 请替换为你的 API token，登录 makuo.cc 用户中心获取。
YOUR_API_TOKEN = 'yixkZjinmtau_zVcPBcBVg' 
BASE_URL = "https://api.makuo.cc/api/get.domain.whois"
DOMAIN_PREFIX = "madespark"
MAX_WORKERS = 8 # 线程数量，可根据你的网络和服务器情况调整

# 这是一个非常全面的顶级域名列表，涵盖了常见的和一些不那么常见的。
tlds = [
    'com', 'cn', 'xyz', 'vip', 'net', 'org', 'info', 'cc', 'tv', 'co', 'me', 'io',
    'online', 'tech', 'store', 'site', 'app', 'dev', 'blog', 'shop', 'art', 'ai',
    'game', 'cloud', 'design', 'wiki', 'live', 'news', 'space', 'fun', 'win', 'link',
    'pro', 'club', 'global', 'group', 'ltd', 'zone', 'rocks', 'systems', 'solutions',
    'digital', 'media', 'services', 'tools', 'ventures', 'company', 'agency',
    'management', 'software', 'technology', 'finance', 'investments', 'holdings',
    'consulting', 'capital', 'partners', 'foundation', 'center', 'institute',
    'academy', 'school', 'university', 'college', 'education', 'training',
    'directory', 'guide', 'business', 'works', 'expert', 'team', 'inc', 'corp',
    'community', 'network', 'city', 'country', 'estate', 'house', 'land',
    'property', 'rentals', 'travel', 'vacations', 'flights', 'hotels', 'tours',
    'events', 'tickets', 'deals', 'discount', 'bargains', 'coupons', 'savings',
    'gmbh', 'gala', 'pizza', 'cafe', 'restaurant', 'bar', 'pub', 'food', 'wine',
    'beer', 'menu', 'kitchen', 'cook', 'recipes', 'delivery', 'express', 'transport',
    'logistics', 'car', 'auto', 'bike', 'motorcycles', 'boats', 'yachts', 'jetzt',
    'reise', 'kaufen', 'verkauf', 'online', 'haus', 'immobilien', 'kredit', 'geld',
    'versicherung', 'steuer', 'recht', 'anwalt', 'arzt', 'zahnarzt', 'klinik',
    'hospital', 'pharmacy', 'health', 'fitness', 'yoga', 'sport', 'run', 'fit',
    'dance', 'music', 'band', 'song', 'album', 'studio', 'video', 'movie', 'film',
    'photography', 'photo', 'pictures', 'gallery', 'camera', 'theater', 'fashion',
    'style', 'beauty', 'makeup', 'hair', 'sucks', 'wtf', 'sex', 'porn', 'adult',
    'xxx', 'love', 'family', 'home', 'wedding', 'marriage', 'baby', 'kids', 'mom',
    'dad', 'family', 'pet', 'dog', 'cat', 'horse', 'animal', 'zoo', 'garden',
    'flowers', 'plants', 'tree', 'forest', 'earth', 'world', 'earth', 'eco', 'green',
    'organic', 'bio', 'farm', 'fishing', 'hunting', 'outdoor', 'camping', 'hiking',
    'ski', 'snow', 'ocean', 'sea', 'beach', 'lake', 'river', 'water', 'desert',
    'mountain', 'valley', 'volcano', 'jungle', 'forest', 'island', 'city', 'town',
    'village', 'capital', 'state', 'country', 'map', 'street', 'road', 'highway',
    'train', 'bus', 'taxi', 'uber', 'lyft', 'auto', 'car', 'bike', 'motorcycles',
    'boats', 'yachts', 'jetzt', 'reise', 'kaufen', 'verkauf', 'online', 'haus',
    'immobilien', 'kredit', 'geld', 'versicherung', 'steuer', 'recht', 'anwalt',
    'arzt', 'zahnarzt', 'klinik', 'hospital', 'pharmacy', 'health', 'fitness',
    'yoga', 'sport', 'run', 'fit', 'dance', 'music', 'band', 'song', 'album',
    'studio', 'video', 'movie', 'film', 'photography', 'photo', 'pictures', 'gallery',
    'camera', 'theater', 'fashion', 'style', 'beauty', 'makeup', 'hair', 'sucks',
    'wtf', 'sex', 'porn', 'adult', 'xxx', 'love', 'family', 'home', 'wedding',
    'marriage', 'baby', 'kids', 'mom', 'dad', 'family', 'pet', 'dog', 'cat', 'horse',
    'animal', 'zoo', 'garden', 'flowers', 'plants', 'tree', 'forest', 'earth',
    'world', 'earth', 'eco', 'green', 'organic', 'bio', 'farm', 'fishing', 'hunting',
    'outdoor', 'camping', 'hiking', 'ski', 'snow', 'ocean', 'sea', 'beach', 'lake',
    'river', 'water', 'desert', 'mountain', 'valley', 'volcano', 'jungle', 'forest',
    'island', 'city', 'town', 'village', 'capital', 'state', 'country', 'map',
    'street', 'road', 'highway', 'train', 'bus', 'taxi', 'uber', 'lyft'
]

def get_whois_info(domain):
    """
    Function to fetch WHOIS information for a single domain.
    Returns a tuple of (domain, data, error_message).
    """
    # Build the full URL with the domain parameter
    url = f"{BASE_URL}?domain={domain}"
    
    # Set the Authorization header with the user's token
    headers = {
        'Authorization': YOUR_API_TOKEN
    }

    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()  # Raises an exception for bad status codes
        data = response.json()
        
        # Check for API-level errors using the 'code' and 'msg' fields
        if data.get("code") != 200:
            return domain, None, data.get("msg", "未知 API 错误")
        
        # Success case: return the domain and its data
        return domain, data.get("data"), None
    
    except requests.exceptions.RequestException as e:
        return domain, None, f"请求失败: {e}"
    except json.JSONDecodeError:
        return domain, None, "无法解析 JSON 响应"
    except Exception as e:
        return domain, None, f"发生未知错误: {e}"

def main():
    """
    Main function to orchestrate the WHOIS lookup process.
    """
    if YOUR_API_TOKEN == 'YOUR_TOKEN_HERE':
        print("请在脚本中设置你的 YOUR_API_TOKEN。")
        return

    # Create the full list of domains to check
    domains_to_check = [f"{DOMAIN_PREFIX}.{tld}" for tld in tlds]
    
    # Use ThreadPoolExecutor for concurrent requests
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        # Submit tasks and wrap the iterator with tqdm for a progress bar
        results = list(tqdm(executor.map(get_whois_info, domains_to_check), total=len(domains_to_check), desc="查询域名 WHOIS 信息"))

    # Process and print the results
    print("\n--- 域名 WHOIS 查询结果 ---")
    
    # Filter for successful results
    success_results = [r for r in results if r[1]]
    
    # Filter for error results
    error_results = [r for r in results if r[2]]

    if success_results:
        print("\n--- 成功获取信息的域名 ---")
        for domain, whois_data, _ in success_results:
            domain_age = whois_data.get("domain_age", "N/A")
            creation_date = whois_data.get("creation_date", "N/A")
            expiration_date = whois_data.get("expiration_date", "N/A")
            registrar = whois_data.get("registrar", "N/A")
            
            print(f"域名: {domain}")
            print(f"  域名年龄: {domain_age}")
            print(f"  创建日期: {creation_date}")
            print(f"  过期日期: {expiration_date}")
            print(f"  注册商: {registrar}")
            print("-" * 20)
            
    if error_results:
        print("\n--- 获取信息失败的域名 ---")
        for domain, _, error_message in error_results:
            print(f"域名: {domain} | 状态: 失败 | 原因: {error_message}")

    print("\n--- 总结 ---")
    print(f"总共查询域名数: {len(domains_to_check)}")
    print(f"成功获取信息的域名数: {len(success_results)}")
    print(f"查询失败的域名数: {len(error_results)}")

if __name__ == "__main__":
    main()