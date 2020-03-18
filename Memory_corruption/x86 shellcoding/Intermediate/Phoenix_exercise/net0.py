#!/usr/bin/python 

from pwn import *

p = remote("localhost", 64010)

def main():
	data = p.recvrepeat(0.2) # Stores reply from svr in variable data
	search_str = "send"

	'''
	Sample output:

	Welcome to phoenix/net-zero, brought to you by https://exploit.education
	Please send '1094664662' as a little endian, 32bit integer.
	'''
	
	for line in data.split("\n"): # Split string by newlines
		if search_str in line: # If search str is in the current line
			# Only interested in the integer part
			integer = line[ line.find("'") +1 : line.rfind("'") ]
			integer = int(integer) # Convert string to integer
			log.info("Data : %d" % integer)

	integer = p32(integer) # Convert integer to little-endian
	p.send(integer)
	
	reply = p.recvrepeat(0.2)
	log.success("%s" % reply)	

if __name__ == "__main__":
	main()
