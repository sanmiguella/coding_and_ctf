#!/usr/bin/python 
from pwn import *

p = remote("localhost", 64012)

def main():
	data = p.recvrepeat(0.5)
	search_str = ["Welcome to phoenix", "For this level"]

	for line in data.split("\n"): # Splits by newline
		# If any of the matched string is in the current line, program doesn't do anything
		if ( search_str[0] in line ) or ( search_str[1] in line ):
			continue
		else:
			real_data = line
			log.info("Length: %d" % len(real_data))
			log.success("Data(packed): %s" % real_data)

	count = 0
	max_count = len(real_data)
	result = 0

	while (count < max_count):
		'''
		If data is "AAAABBBBCCCCDDDD", then data will be split into:
		AAAA
		BBBB
		CCCC
		DDDD	
		'''
		# Slice string into pieces of 4 bytes 
		four_byte_data = real_data[count : count +4] 
		four_byte_data = u32(four_byte_data) # Unpacks it into integer
		
		# Each unpacked integer will get added to the total sum(result)
		result = result + four_byte_data 
			
		# Program will loop 4 times since the max length is 16	
		count = count +4 	
	
	log.success("Data(unpacked): %s" % str(result))	

	# Handle integer overflow by doing a logical AND with 0xffffffff
	result &= 0xffffffff 

	# Converts results to little endian to be send to the server
	result_packed = p32(result) 
	p.sendline(result_packed) # Sends packed results to the server
	
	reply = p.recvline()
	log.success("Reply: %s" %reply)
				

if __name__ == "__main__":
	main()
