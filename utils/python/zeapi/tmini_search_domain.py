import requests
import json
import concurrent.futures
import time
from tqdm import tqdm
from functools import wraps
import threading # 导入 threading 模块来使用 Lock

# --- Configuration ---
# 请替换为你的 API 秘钥（Key）
YOUR_API_KEY = 'WGKJ92GS80OH8X4WRCHO'
BASE_URL = "https://www.tmini.net/api/getPrices"
DOMAIN_PREFIX = "madespark"
MAX_WORKERS = 8 # 最大并发线程数，可根据网络情况调整
MAX_CALLS_PER_MINUTE = 50 # 限制在 60 次/分钟以下，留出余量

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

# 用于频率限制的全局状态
request_count = 0
start_time = time.time()
rate_limit_lock = threading.Lock() # 修复：使用 threading.Lock()

def rate_limited(max_calls, period=60.0):
    """
    一个简单的装饰器，用于限制函数在指定时间段内的调用次数。
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            global request_count, start_time
            with rate_limit_lock:
                # 检查是否需要重置计数器
                current_time = time.time()
                elapsed_time = current_time - start_time
                if elapsed_time > period:
                    request_count = 0
                    start_time = current_time
                
                # 如果超过限制，则等待
                if request_count >= max_calls:
                    wait_time = period - elapsed_time
                    tqdm.write(f"达到速率限制，等待 {wait_time:.2f} 秒...")
                    time.sleep(wait_time)
                    request_count = 0
                    start_time = time.time()
                
                request_count += 1
            return func(*args, **kwargs)
        return wrapper
    return decorator

@rate_limited(MAX_CALLS_PER_MINUTE)
def get_domain_price(domain):
    """
    Function to fetch pricing for a single domain.
    Returns a tuple of (domain, price_data, error_message).
    """
    tld = domain.split('.')[-1]
    url = f"{BASE_URL}?ckeystring={YOUR_API_KEY}&sld={tld}"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raises an exception for bad status codes
        data = response.json()
        
        # Check for API-level errors
        if data.get("success") is not True:
            return domain, None, data.get("msg", "API 返回未知错误")
        
        # Check price status
        if data.get("registered") is True:
             return domain, None, "域名已被注册"
        else:
            return domain, data.get("price"), None

    except requests.exceptions.RequestException as e:
        return domain, None, f"请求失败: {e}"
    except json.JSONDecodeError:
        return domain, None, "无法解析 JSON 响应"
    except Exception as e:
        return domain, None, f"发生未知错误: {e}"

def main():
    """
    Main function to orchestrate the domain price checking.
    """
    if YOUR_API_KEY == 'YOUR_API_KEY_HERE':
        print("请在脚本中设置你的 YOUR_API_KEY。")
        return

    # Create the full list of domains to check
    domains_to_check = [f"{DOMAIN_PREFIX}.{tld}" for tld in tlds]
    
    # Use ThreadPoolExecutor for concurrent requests
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        # Submit tasks and wrap the iterator with tqdm for a progress bar
        results = list(tqdm(executor.map(get_domain_price, domains_to_check), total=len(domains_to_check), desc="查询域名价格"))

    # Process and print the results
    print("\n--- 域名价格查询结果 ---")
    
    # Filter for successful results (price data exists)
    success_results = [r for r in results if r[1] is not None]
    
    # Filter for error results
    error_results = [r for r in results if r[2] is not None]

    if success_results:
        print("\n--- 可注册的域名及其价格 ---")
        for domain, price_data, _ in success_results:
            price = price_data.get("register") if price_data else "N/A"
            print(f"域名: {domain} | 价格: {price}")
            
    if error_results:
        print("\n--- 无法获取价格或已注册的域名 ---")
        for domain, _, error_message in error_results:
            print(f"域名: {domain} | 状态: 失败/已注册 | 原因: {error_message}")

    print("\n--- 总结 ---")
    print(f"总共查询域名数: {len(domains_to_check)}")
    print(f"成功获取价格的域名数: {len(success_results)}")
    print(f"查询失败或已注册的域名数: {len(error_results)}")


if __name__ == "__main__":
    main()