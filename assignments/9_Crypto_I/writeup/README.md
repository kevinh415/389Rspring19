# Crypto I Writeup

Name: Chaewoon Hong
Section: 0201

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Chaewoon Hong

## Assignment Writeup

### Part 1 (70 Pts)
I used a dict to store the hashes from hashes.txt. I set the keys as the hash and the value as an empty string that I could fill out later. During the loop, I checked to see if the generated hash was in my dict. If it was, then I set the value of that hash to the character/password combination. Finally, I ran a loop through the dict to print out the input and output. 

### Part 2 (30 Pts)
This was similar to part 1 where I had to generate the hashes and compare it with what the server gave me. I ran a loop three times and sent the correct input when I found a match. After the loop, I did another retrieval to get the flag. 
FLAG: CMSC389R-{h@sh1ng_@nd_sl@sh1ng}


