.globl _start
_start:
	jmp do_call
jmp_back:
	xor %eax, %eax # zeroes eax
	xor %ebx, %ebx # zeroes ebx
	xor %ecx, %ecx # zeroes ecx
	xor %edx, %edx # zeroes edx

	#4	sys_write	0x04	unsigned int fd	const char __user *buf	size_t count
	movb $4, %al # Assigns 4 to eax
	movb $1, %bl # Assigns 1 to ebx
	popl %ecx # pop /bin/sh off the stack to ecx
	movb $8, %dl # Assigns 8 to edx
	int $0x80 # Call kernel

	#1	sys_exit	0x01	int error_code
	xor %eax, %eax	# zeroes eax
	movb $1, %al # Assigns value 1 to eax
	xor %ebx, %ebx # zeroes ebx register, exit success
	int $0x80 # Call kernel
do_call:
	call jmp_back
binsh:
	.ascii "/bin/sh\n"
