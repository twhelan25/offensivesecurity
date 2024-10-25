import socket
import os

# Get the IP address from the environment variable
host = os.environ.get('ip')
if not host:
    print("Error: Environment variable 'ip' is not set")
    exit(1)

port = 8000

wordlist = "/usr/share/wordlists/dirb/common.txt"

def fuzz_endpoint(wordlist):
    try:
        with open(wordlist, 'r') as file:
            for line in file:
                command = line.strip()
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((host, port))
                    s.sendall(command.encode() + b'\n')
                    response = s.recv(1024).decode().strip()
                    if response != "" and "is not defined" not in response and "leading zeros" not in response:
                        print(f"Response {response}")
    except FileNotFoundError:
        print(f"File doesn't exist")
    except socket.gaierror:
        print(f"Address-related error connecting to server: {host}")
    except socket.error as e:
        print(f"Connection error: {e}")

fuzz_endpoint(wordlist)
