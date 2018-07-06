#Bguess-1-0
Bguess is a very simple python tool that comes in handy specially when playing around [CTFS].
most of the time ctf host will provide some challenges including base(XX) encoded text.in this case Bguess will save time searching for the right decoding base,
it simply does a "decoding-bruteforce" on the encoded txt with 8 different decoding bases and displays the result instantly.
Bguess Supports:
-Base16
-Base32
-Base58
-Base62
-Base64
-ASCII85
-Base85
-Base91


Usage 
python3 bguess.py encoded_txt

Example : CSAW-CTF-2016-Quals -> Forensics -> Watchword
Writeup : https://github.com/isislab/CSAW-CTF-2016-Quals/tree/master/Forensics/Watchword
by using Bguess
python3 bguess.py 'W^7?+dsk&3VRB_4W^-?2X=QYIEFgDfAYpQ4AZBT9VQg%9AZBu9Wh@|fWgua4Wgup0ZeeU}c_3kTVQXa}eE'
output: b'flag{We are fsociety, we are finally free, we are finally awake!}'
