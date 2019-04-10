#!/usr/bin/env python2

import sys
import struct
from datetime import datetime

# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


# Some constants. You shouldn't need to change these.
MAGIC = 0x8BADF00D
VERSION = 1
counter = 8

if len(sys.argv) < 2:
    sys.exit("Usage: python stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version = struct.unpack("<LL", data[0:counter])
# counter is 8

time, extra = struct.unpack("<LL", date[counter: counter + 8])
counter += 4 # counter is 12 

author = ''.join(struct.unpack("<8s", data[counter: counter + 8]))
counter += 8 # add 8 because author is 8 bytes - counter is 12

section_count, extra = struct.unpack("<LL", data[counter: counter + 8])
counter += 4



if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))
print("DATE: " + str(datetime.utcfromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')))
print("AUTHOR: " + author)
print("SECTION COUNT: " + str(section_count))


# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!

print("-------  BODY  -------")
for i in range(section_count):
	stype, extra = struct.unpack("<LL", data[counter: counter + 8])
	counter += 4
	slen, extra = struct.unpack("<LL", data[counter: counter + 8])
	counter += 4

	stype = int(stype)
	print("stype: " + str(stype))
	if (stype == 1):
		s = str(slen) + "s"
		val = struct.unpack(s, data[counter: counter + int(slen)])
		counter += int(slen)
		print(val)
	elif (stype == 2):
		s = str(slen) + "s"
		val = struct.unpack(s, data[counter: counter + int(slen)])
		counter += int(slen)
		print(val.decode('utf-8'))
	elif (stype == 3):
		n = int(slen) / 4
		val = struct.unpack(n, data[counter: counter + n])
		counter += n
		print(val)
	elif (stype == 4):
		n = int(slen) / 8
		val = struct.unpack(n, data[counter: counter + n])
		counter += n
		print(val)
	elif (stype == 5):
		n = int(slen) / 8
		val = struct.unpack(n, data[counter: counter + n])
		counter += n
		print(val)
	elif (stype == 6):
		if(int(slen) == 16):
			val = struct.unpack("dd", data[counter: counter + 16])
			print(val)
		else:
			bork("fail")
		counter += 16
	elif (stype == 7):
		if(int(slen) == 4):
			val = struct.unpack("L", data[counter: counter + 4])
			print(val)
		else:
			bork("fail")
		counter += 4
	elif (stype == 8):
		s = str(slen) + "s"
		file = "pic.png"
		f = open(file, "wb")
		f.write(bytes([137,80,78,71,13,10,26,10]))
		val = struct.unpack(s, data[counter: counter + slen])
		counter += slen
		f.write(val[0])
		f.close()
	elif (stype == 9):
		s = str(slen) + "s"
		file = "gif.gif"
		f = open(file, "wb")
		f.write(bytes([47,49,46,38,37,61]))
		val = struct.unpack(s, data[counter: counter + slen])
		counter += slen
		f.write(val[0])
		f.close()
	elif (stype == 10):
		s = str(slen) + "s"
		file = "gif.gif"
		f = open(file, "wb")
		f.write(bytes([47,49,46,38,37,61]))
		val = struct.unpack(s, data[counter: counter + slen])
		counter += slen
		f.write(val[0])
		f.close()
