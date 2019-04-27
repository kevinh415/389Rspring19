#!/usr/bin/env python3

import hashlib
import string

def crack():
    hashes = open("hashes.txt","r").readlines() # open and read hashes.txt
    passwords = open("passwords.txt", "r").readlines() # open and read passwords.txt
    characters = string.ascii_lowercase

    dict = {}

    for line in hashes:
	line = line.strip()
        dict[line] = ""

    for c in characters:
        for p in passwords:
            # crack hashes
	    text = (c+p).strip()
            h = hashlib.sha256(text.encode()).hexdigest()
            if h in dict.keys():
                dict[h] = text

    for k in dict:
	print(dict[k] + ":" + k)


if __name__ == "__main__":
    crack()
