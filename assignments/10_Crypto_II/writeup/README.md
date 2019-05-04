# Crypto II Writeup

Name: Chaewoon Hong
Section: 0201

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Chaewoon Hong

## Assignment Writeup

### Part 1 (70 Pts)
Using the information from the slides, I used gpg to import key.asc and to decrypt message.txt.gpg. After decrypting the message (gpg --decrypt message.txt.gpg), I found the flag CMSC389R-{m3ss@g3_!n_A_b0ttl3}. 

Following the instructions from the decrypted message, I created a new signature.txt file and used the command "gpg --clearsign signature.txt" to produce the signature.txt.asc file. 

(screenshot provided in the files)

### Part 2 (30 Pts)

I followed the instructions from the READ.ME and ran the fix.sh script.

1. What do you notice about both pictures?
	
	I noticed that the ecb.bmp still resembles the original image while cbc.bmp looks like random colored pixels that do not resemble the original image.
2. Which block cipher mode is less secure? Why? Explain using information about
   how the different block cipher modes of operation work.
	
	ecb is less secure because the image still somewhat resembles the original image. This is because the process of ecb involves encrypting a block of input and outputting the block of output independently for each block. On the other hand, cbc involves the block of input interacting with the previous outputted block during the encruption process, which means that each block is dependent of the other blocks. This adds a level of complexity that ecb does not have, which makes it more secure.

