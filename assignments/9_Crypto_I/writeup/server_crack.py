#!/usr/bin/env python3

import hashlib
import string
import socket
import time

def server_crack():
    hashes = open("hashes.txt","r").readlines() # open and read hashes.txt
    passwords = open("passwords.txt", "r").readlines() # open and read passwords.txt
    characters = string.ascii_lowercase
    server_ip = '134.209.128.58'
    server_port = 1337

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, server_port))

    for i in range(0,3):
        data = s.recv(1024)

        hash = data.splitlines()[2]
        print(hash)

        for c in characters:
            for p in passwords:
                # crack hashes
	        text = (c+p).strip()
                h = hashlib.sha256(text.encode()).hexdigest()
	        if hash == h:
	            print(text)
		    s.send(text+"\n")
		    time.sleep(1)

    data = s.recv(1024)
    print(data)


if __name__ == "__main__":
    server_crack()
