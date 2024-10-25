import socket
from termcolor import colored  # Requires `pip install termcolor`

host = '$ip'
port = 8000
wordlist = "/usr/share/wordlists/dirb/common.txt"

# Function to display valid endpoint in color
def display_valid_endpoint(endpoint):
    print(colored(f"Valid Endpoint Found: {endpoint}", "green", attrs=["bold"]))

# Set up request to endpoint
def fuzz_endpoint(wordlist):
    unique_responses = set()  # To keep track of unique responses
    try:
        # Open wordlist
        with open(wordlist, 'r') as file:
            for line in file:
                # Clean up new lines
                command = line.strip()

                # Establish connection to the server
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((host, port))

                    # Send fuzzing to target
                    s.sendall(command.encode() + b'\n')

                    # Receive the response
                    response = s.recv(1024).decode().strip()

                    # Logic to catch valid response and avoid duplicates
                    if response and response not in unique_responses:
                        unique_responses.add(response)
                        if "is not defined" not in response and "leading zeros" not in response:
                            display_valid_endpoint(response)
                        else:
                            print(f"Response: {response}")

    except FileNotFoundError:
        print("File doesn't exist")
    except Exception as e:
        print(f"An error has occurred: {e}")

fuzz_endpoint(wordlist)
