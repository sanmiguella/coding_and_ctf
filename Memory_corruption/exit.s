.globl _start
_start:
	#			eax 	ebx
	#	sys_exit	0x01	int error_code

	xor %eax, %eax # Zero'es eax register
	movb $1, %al # Assigns value 1 to eax register
	
	xor %ebx, %ebx # Zero'es ebx 
	int $0x80 # Calls kernel	
