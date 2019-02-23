# Writeup 2 - OSINT

Name: Chae woon Hong
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: Chae woon Hong

## Assignment Writeup

### Part 1 (45 pts)

1. v0idcache's real name is Elizabeth Moffet. 
2. v0idcache works at 13/37th National Bank. The website is http://1337bank.money.
3. Twitter: @v0idcache URL: https://twitter.com/v0idcache
   Github: @v0idcache URL: https://github.com/v0idcache
I discovered these accounts by adding /v0idcache to the URL.
4. 142.93.136.81
	The location is Amsterdam in Netherlands
5. {h1ding_fil3s_in_r0bots_L0L} - robots.txt and then going to /secret_directory
   {h1dd3n_1n_plain_5ight} - page source
6. Ports 22, 80, and 1337 are open. I discovered this using www.t1shopper.com/tools/port-scan. I typed in the IP address and the port range 1-3000.
7. The website is running on Ubuntu. I discovered this through censys.io.
8. 
{h0w_2_iNt0_DNS_r3c0Rd5} - centralops.net
{YWx$H3d3Bz6dx9IG32Odv0JZh - AB4300.txt
{brut3_f0rce_m4ster} - flag.txt



### Part 2 (75 pts)

First I extracted rockyou.txt from rockyou.txt.gz. Then I iterated through each line in rockyou.txt. Everytime I iterated through a line, I renewed the socket connection. The first recovery was for inputting the username, which was always "v0idcache" with a new line. The next recovery was the password, which I set as the current line of text. If the third recovery said "Fail", then the code keeps looping through the lines in rockyou.txt until the output is not "Fail". Once the output is not "Fail", the code breaks and outputs the correct password.
