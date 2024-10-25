import socket
import os

host = os.environ.get('ip')
if not host:
    print("Error: Environment variable 'ip' is not set")
    exit(1)

port = 8000

wordlist = "/usr/share/wordlists/dirb/common.txt"

def fuzz_endpoint(wordlist):
    unique_responses = set()  # Use a set to store unique responses
    try:
        with open(wordlist, 'r') as file:
            for line in file:
                command = line.strip()
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((host, port))
                    s.sendall(command.encode() + b'\n')
                    response = s.recv(1024).decode().strip()
                    if response and "is not defined" not in response and "leading zeros" not in response:
                        # Only add and print unique responses
                        if response not in unique_responses:
                            unique_responses.add(response)
                            print(f"Command: {command}")
                            print(f"Unique Response: {response}\n")
    except FileNotFoundError:
        print(f"File doesn't exist")
    except Exception as e:
        print(f"Error has occurred: {e}")

fuzz_endpoint(wordlist)
