#!/usr/bin/python 

from pwn import *  

# Starts process 
p = remote("localhost", 64011)

def main(): 
	data = p.recvrepeat(0.2) # Stores reply from server into variable
	search_str = "Welcome to phoenix"
	
	for line in data.split("\n"):
		# If "Welcome to phoenix" is in the current line,
		# program will skip
		if search_str in line:
			continue 
		else:
			data = u32(line) # Converts string to integer
			log.info("Got data: %d" % data)
			
			p.sendline(str(data)) # Sends data to the server

	reply = p.recvline() # Receives data from the server	
	log.info("%s" %reply)
			
if __name__ == "__main__": 
	main()
