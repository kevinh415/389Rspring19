# Crypto II Writeup

Name: Chaewoon Hong
Section: 0201

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Chaewoon Hong

## Assignment Writeup

### Part 1 (40 Pts)
While browsing the website, I noticed that the URL for the items changed for each element. There was a '/item?id=' appended to the original URL with incrementing numbers after 'id='. Using the slides, I was finally able to display all the contents by adding a 1'='1 along with a '||' before it. 

The flag was CMSC389R-{y0u_ar3_th3_SQ1_ninj@}.

### Part 2 (60 Pts)

Level 1: I added <script>alert()</script> into the url. 

Level 2: I noticed that when i added a '<h1>' element, the text behaved according to the h1 element, so I added a onerror=alert() into the h1 tag. 

Level 3: I noticed the URL could be injected so I added a 'onerror='alert(1)'; to the URL.

Level 4: The URL changed when the timer was active, so using the URL that was changed, I was able to add a ')%3Balert(' to the timer to get the error. 

Level 5: In the URL where it says next=confirm, I just changed confirm to javascript:alert();.

Level 6: Using the hint, I used the URL google.com/jsapi?callback= to set it to 'alert' after the '=' sign. I removed the /static/gadget.js from the URL and appended the google URL after adding another '/'.
