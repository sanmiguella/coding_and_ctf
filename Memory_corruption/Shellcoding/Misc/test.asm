global _start

section .text

_start:
	; Zeroes register eax ~ edx
	xor eax,eax
	xor ebx,ebx
	xor ecx,ecx
	xor edx,edx

	mov al,0x4 ; syscall # for write
	mov bl,0x1 ; fd 1 : stdout
	mov ecx,message ; address of DEADBEEF to ecx
	mov dl,mlen ; length of DEADBEEF
	int 0x80 

	; Zeroes register eax ~ edx
	xor eax,eax
	xor ebx,ebx
	xor ecx,ecx
	xor edx,edx 
	
	; Exit with value 6
	mov al,0x1 ; syscall # for exit
	mov bl,0x6 ; exit # : 6
	int 0x80 ; calls kernel

section .data	
	message db 0x44,0x45,0x41,0x44,0x42,0x45,0x45,0x46 ; DEADBEEF
	mlen equ $-message
