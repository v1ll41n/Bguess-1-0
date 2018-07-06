#Bguess-1-0<br/>
Bguess is a very simple python tool that comes in handy specially when playing around [CTFS].  <br/>
most of the time ctf host will provide some challenges including base(XX) encoded text.in this case Bguess will save time searching for the right decoding base, <br/>
it simply does a "decoding-bruteforce" on the encoded txt with 8 different decoding bases and displays the result instantly. <br/>
Bguess Supports:  <br/>
-Base16<br/>
-Base32<br/>
-Base58<br/>
-Base62<br/>
-Base64<br/>
-ASCII85<br/>
-Base85<br/>
-Base91<br/>


Usage <br/>
python3 bguess.py encoded_txt <br/>

Example : CSAW-CTF-2016-Quals -> Forensics -> Watchword <br/>
Writeup : https://github.com/isislab/CSAW-CTF-2016-Quals/tree/master/Forensics/Watchword  <br/>
by using Bguess  <br/>
python3 bguess.py 'W^7?+dsk&3VRB_4W^-?2X=QYIEFgDfAYpQ4AZBT9VQg%9AZBu9Wh@|fWgua4Wgup0ZeeU}c_3kTVQXa}eE'  <br/>
output: b'flag{We are fsociety, we are finally free, we are finally awake!}' <br />
<img src=Bguess.png />
