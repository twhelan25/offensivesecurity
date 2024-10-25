import socket
import sys

# Check if IP address is provided as argument
if len(sys.argv) < 2:
    print("Please provide the IP address as an argument")
    sys.exit(1)

host = sys.argv[1]  # Get the IP address from command line argument
port = 8000

wordlist = "/usr/share/wordlists/dirb/common.txt"

# Rest of your script remains the same
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
    except Exception as e:
        print(f"Error has occurred: {e}")

fuzz_endpoint(wordlist)
