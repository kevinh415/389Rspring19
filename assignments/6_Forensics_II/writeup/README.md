# Writeup 6 - Forensics

Name: Chae woon Hong
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *PUT YOUR NAME HERE*

## Assignment Writeup

### Part 1 (45 Pts)

1. 142.93.136.81 is the IP address that has been hacked. I found this by looking at the "Destination" column where the "info" column had the user requests.

2. The attackers were using nmap to scan the ports. 
 
3. Hackers' IP address: 159.203.113.181. They were connecting from Clifton, New Jersey. I found this information by using www.iptrackeronline.com. 

4. They were using Port 21. I found this by using Follow -> TCP stream, clicking on one of the lines with the user request, and scrolling down the middle row until I saw "Transmissino Control Protocol, Src Port: 55914, Dst Port: 21".

5. They stole the file fine_me.jpeg from the server. I found this information from the TCP stream where the line said "RETR find_me.jpeg." "RETR" stands for "retrieve", which means that the attackers retrieved the file from the server. 

	The file was a jpeg file. 
	The photo was taken in The Hand, Rambla General Artigas, 20100 Punta Del Este, Uruguay. I found this info by using on online photo metadata website (metapicz) and inputting the lat and long into gps-coordinates.net. 
	The photo was taken in 12/23/2018 at 5:16:24 pm. This information was from metapicz.com. 
	The photo was taken by an iPhone 8. This information was from metapicz.com. 
	The photo was taken 4.57 meters below sea level. I found this information from metapicz.com. 

6. The attackers left the file greetz.fpff. Using Wireshark, I found out that the user inputted the command "STOR greetz.fpff to the server. "STOR" is short for "STORE", which meant that the user stored this file onto the server. 
	
7. A countermeasure to prevent this kind of intrusion from happening again is to use a firewall to block all incoming packets except for specific IP addresses.



### Part 2 (55 Pts)

1. I used a counter to keep track of the location of the bytes. I had to be careful when incrementing the counter because some words like author required 8 bytes while other words like time only required 4. I looped through the sections in section_count and used if statements to appropriately handle each case. 


2. Greetz.fpff was generated on 3/27/2019 at 4:15:05. Fl1nch authored greetz.fpff. 

Section 1 (ASCII): Hey you, keep looking :)
Section 6 (Coord): (52.336035, 4.990673)
Section 8 (PNG): contains an image
Section 1 (ASCII): R983CSMC_perg_tndid_u0y_yllufep0h{-R983CSMC
Section 1 (ASCII): Q01TQzM4OVIte2hleV9oM3lfeTBVX3lvdV9JX2RvbnRfbGlrZV95b3VyX2Jhc2U2NF9lbmNvZGluZ30=


FLAG: CMSC389R-{h0pefully_y0u_didnt_grep_CMSC389R}
