#!/usr/bin/python3

import sys,base64,base91,base62,base58

print( '''

 ######                              #####                              
 #     #   ##    ####  ######       #     # #    # ######  ####   ####  
 #     #  #  #  #      #            #       #    # #      #      #      
 ######  #    #  ####  #####  ##### #  #### #    # #####   ####   ####  
 #     # ######      # #            #     # #    # #           #      # 
 #     # #    # #    # #            #     # #    # #      #    # #    # 
 ######  #    #  ####  ######        #####   ####  ######  ####   ####  
                                                                        

''')

def bguess(encoded) :
    try:
     print ("[+] base91 : ->" , base91.decode(encoded),"\n")
    except: 
     print ("[-] base91 : ->  Invalid\n")
    try:
     print ("[+] base85 : ->" , base64.b85decode(encoded),"\n")
    except: 
     print ("[-] base85 : ->  Invalid\n")
    try:
     print ("[+] ASCII85 : -> " , base64.a85decode(encoded),"\n")
    except: 
     print ("[-] ASCII85 : ->  Invalid\n")
    try:
     print ("[+] base64 : ->" , base64.b64decode(encoded),"\n")
    except: 
     print ("[-] base64 : ->  Invalid\n")
    try:
     print ("[+] base62 : ->" , base62.decode(encoded),"\n")
    except: 
     print("[-] base62 : ->  Invalid\n")
    try:
     print ("[+] base58 : ->" , base58.b58decode(encoded),"\n")
    except: 
     print ("[-] base58 : -> \n")
    try:
     print ("[+] base32 : ->" , base64.b32decode(encoded),"\n")
    except: 
     print ("[-] base32 : -> Invalid\n")
    try:
     print ("[+] base16 : ->" , base64.b16decode(encoded),"\n")
    except:   
     print ("[-] base16 : -> Invalid\n")

try:
 encoded=sys.argv[1]
except: 
 print ("encoded input is missing!\n")
 exit()

bguess(encoded)
'''
try:
 print ("[+] base92 : ->" , base64.decode(encoded),"\n")
except: 
 print ("[-] base92 : ->  Invalid\n"
'''

