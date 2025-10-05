import requests
import json
import concurrent.futures
from tqdm import tqdm

# Hardcoded list of domain suffixes (TLDs).
# 这是一个非常全面的列表，涵盖了常见的和一些不那么常见的顶级域名。
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

BASE_URL = "https://zeapi.ink/v1/api/whois"
DOMAIN_PREFIX = "madespark"
CURRENCY = "USD"
MAX_WORKERS = 8

def get_domain_price(domain):
    """
    Function to fetch pricing for a single domain.
    Returns a tuple of (domain, price_data, error_message).
    """
    url = f"{BASE_URL}?domain={domain}&cy={CURRENCY}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raises an exception for bad status codes
        data = response.json()
        
        # Check for API-level errors
        if data.get("status") == "error":
            return domain, None, data.get("message", "Unknown API error")
        
        # Check price status
        price_status = data.get("price", {}).get("status")
        if price_status == "success":
            price_data = data["price"]["data"]
            # Check if domain is available (price data exists)
            if price_data:
                return domain, price_data, None
            else:
                return domain, None, "Price data not available (domain taken or other issue)"
        else:
            return domain, None, data.get("price", {}).get("message", "Price check failed")

    except requests.exceptions.RequestException as e:
        return domain, None, f"Request failed: {e}"
    except json.JSONDecodeError:
        return domain, None, "Failed to decode JSON response"
    except Exception as e:
        return domain, None, f"An unexpected error occurred: {e}"

def main():
    """
    Main function to orchestrate the domain price checking.
    """
    # Create the full list of domains to check
    domains_to_check = [f"{DOMAIN_PREFIX}.{tld}" for tld in tlds]
    
    # Use ThreadPoolExecutor for concurrent requests
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        # Submit tasks and wrap the iterator with tqdm for a progress bar
        results = list(tqdm(executor.map(get_domain_price, domains_to_check), total=len(domains_to_check)))

    # Process and print the results
    print("\n--- Domain Price Check Results ---")
    
    # Filter for successful results
    success_results = [r for r in results if r[1]]
    
    # Filter for error results
    error_results = [r for r in results if r[2]]

    if success_results:
        print("\n--- Domains with Price Data ---")
        for domain, price_data, _ in success_results:
            new_price = price_data.get("new", "N/A")
            renew_price = price_data.get("renew", "N/A")
            currency = price_data.get("currency_symbol", "")
            print(f"Domain: {domain} | New Price: {currency}{new_price} | Renew Price: {currency}{renew_price}")
            
    if error_results:
        print("\n--- Domains with Errors/Unavailable ---")
        for domain, _, error_message in error_results:
            print(f"Domain: {domain} | Status: Failed | Reason: {error_message}")

    print("\n--- Summary ---")
    print(f"Total domains checked: {len(domains_to_check)}")
    print(f"Domains with price data: {len(success_results)}")
    print(f"Domains with errors: {len(error_results)}")


if __name__ == "__main__":
    main()