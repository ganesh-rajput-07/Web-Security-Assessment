import re
import requests

def check_sql_injection(url):
    """Check if a given URL is vulnerable to SQL Injection."""
    test_payload = "' OR '1'='1"
    test_url = f"{url}?input={test_payload}"
    
    try:
        response = requests.get(test_url, timeout=5)
        if "error" in response.text.lower() or "syntax" in response.text.lower():
            print("[!] Potential SQL Injection vulnerability detected!")
        else:
            print("[-] No SQL Injection vulnerability detected.")
    except requests.exceptions.RequestException as e:
        print("[ERROR] Could not connect to the target URL.", str(e))

# Example usage
if __name__ == "__main__":
    target_url = input("Enter the target URL: ")
    check_sql_injection(target_url)
