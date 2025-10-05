import requests
import json

# --- Configuration ---
# Replace with your API token
YOUR_API_TOKEN = 'yixkZjinmtau_zVcPBcBVg'
BASE_URL = "https://api.makuo.cc/api/get.domain.whois"
DOMAIN_TO_CHECK = "madespark.com"

def get_single_whois_info():
    """
    Fetches and prints WHOIS information for a single, specified domain.
    """
    if not YOUR_API_TOKEN:
        print("Error: API token not set. Please update the YOUR_API_TOKEN variable.")
        return

    # Build the full URL with the domain parameter
    url = f"{BASE_URL}?domain={DOMAIN_TO_CHECK}"
    
    # Set the Authorization header with the user's token
    headers = {
        'Authorization': YOUR_API_TOKEN
    }

    print(f"Attempting to query WHOIS for domain: {DOMAIN_TO_CHECK}\n")
    print(f"Request URL: {url}")
    print(f"Authorization Header: {headers}\n")

    try:
        response = requests.get(url, headers=headers, timeout=15)
        
        # Check for HTTP status codes
        response.raise_for_status()
        
        # Parse the JSON response
        data = response.json()
        
        # Print the raw JSON data for full context
        print("--- API Response (Raw) ---")
        print(json.dumps(data, indent=4, ensure_ascii=False))
        
        # Check the API's internal status code (200 for success)
        if data.get("code") == 200:
            whois_data = data.get("data", {})
            print("\n--- WHOIS Information Found ---")
            print(f"Domain: {whois_data.get('domain', 'N/A')}")
            print(f"Domain Age: {whois_data.get('domain_age', 'N/A')}")
            print(f"Creation Date: {whois_data.get('creation_date', 'N/A')}")
            print(f"Expiration Date: {whois_data.get('expiration_date', 'N/A')}")
            print(f"Registrar: {whois_data.get('registrar', 'N/A')}")
        else:
            print("\n--- API Error ---")
            print(f"Status Code: {data.get('code', 'N/A')}")
            print(f"Message: {data.get('msg', 'N/A')}")

    except requests.exceptions.HTTPError as http_err:
        print(f"\n--- HTTP Error ---")
        print(f"An HTTP error occurred: {http_err}")
        print(f"The server responded with status code: {response.status_code}")
        print(f"Response Body: {response.text}")
    except requests.exceptions.RequestException as req_err:
        print(f"\n--- Request Error ---")
        print(f"A request error occurred: {req_err}")
    except json.JSONDecodeError:
        print(f"\n--- JSON Decode Error ---")
        print("Failed to decode JSON from the response.")
    except Exception as err:
        print(f"\n--- Unexpected Error ---")
        print(f"An unexpected error occurred: {err}")

if __name__ == "__main__":
    get_single_whois_info()