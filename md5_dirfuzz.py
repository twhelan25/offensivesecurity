import requests
import time

# IP address
ip = "10.10.143.116"

def check_directory(number):
    md5_hash = format(number, '032x')  # Convert number to 32-character hex string
    url = f"http://{ip}/{md5_hash}"
    try:
        response = requests.get(url, timeout=5)
        return response.status_code, response.text.strip()
    except requests.RequestException:
        return None, None

print("Starting scan...")

# Scan directories 0-50 and report any content, especially if it contains 'flag'
for i in range(51):
    print(f"Checking directory {i}...", end='', flush=True)
    status, content = check_directory(i)
    
    if status is None:
        print(" Error (connection failed)")
    elif content:
        print(f" Content found!")
        print(f"Directory {i} (MD5: {format(i, '032x')}):")
        print(f"Status: {status}")
        print(f"Content: {content[:100]}...")  # Print first 100 characters of content
        if 'flag' in content.lower():
            print("FLAG FOUND IN THIS DIRECTORY!")
        print()  # Empty line for readability
    else:
        print(f" Status: {status}, No content")
    
    time.sleep(1)  # Add a 1-second delay between requests to be polite to the server

print("Scan complete.")
