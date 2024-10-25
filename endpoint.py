import socket
import os

# Get the IP address from the environment variable
host = os.environ.get('ip')
if not host:
    print("Error: Environment variable 'ip' is not set")
    exit(1)

print(f"Attempting to connect to: {host}")  # Debug print

port = 8000

wordlist = "/usr/share/wordlists/dirb/common.txt"

def fuzz_endpoint(wordlist):
    try:
        print(f"Opening wordlist: {wordlist}")  # Debug print
        with open(wordlist, 'r') as file:
            for line in file:
                command = line.strip()
                print(f"Trying command: {command}")  # Debug print
                try:
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                        s.settimeout(5)  # Set a timeout of 5 seconds
                        print(f"Connecting to {host}:{port}")  # Debug print
                        s.connect((host, port))
                        s.sendall(command.encode() + b'\n')
                        response = s.recv(1024).decode().strip()
                        if response != "" and "is not defined" not in response and "leading zeros" not in response:
                            print(f"Response: {response}")
                            print(f"Command {command}")
                except socket.timeout:
                    print(f"Connection to {host}:{port} timed out")
                except socket.error as e:
                    print(f"Socket error occurred: {e}")
    except FileNotFoundError:
        print(f"File doesn't exist: {wordlist}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

fuzz_endpoint(wordlist)
