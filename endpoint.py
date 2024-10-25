import socket
import os

host = '$ip'
port = 8000

wordlist = "/usr/share/wordlists/dirb/common.txt"

# set up request to endpoint
def fuzz_endpoint(wordlist):
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

                    # Logic to catch valid response
                    if response != "" and "is not defined" not in response and "leading zeros" not in response:
                        print(f"Response {response}") 

    except FileNotFoundError:
        print(f"File doesn't exist")
    except Exception as e:
        print(f"Error has occurred {e}")

fuzz_endpoint(wordlist)
