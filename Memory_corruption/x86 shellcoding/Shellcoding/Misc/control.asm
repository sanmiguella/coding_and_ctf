global _start
section .text

_start:
	mov al,0x2	  ; Stores the value 2 in the eax register
	jmp DisplayBanner ; Jump to DisplayBanner()

DisplayBanner:
	push eax 	; Stores value of eax into the stack

	; Writes custom message to the console
	; write(1,message,message_length)
	mov al,0x4 	; Syscall for write
	mov bl,0x1 	; File descriptor, 1 : Stdout
	mov ecx,message ; Message to be displayed 
	mov dx,mlen 	; Length of the message
	int 0x80 	; Calls kernel

	pop eax 	  ; Pops value from the stack to eax 
	dec eax		  ; Decrement eax by 1	
	test eax, eax	  ; Check if eax is zero
	jnz DisplayBanner ; If eax is 0, jump to PopShell()	

PopShell:
	; Zeroes the register eax,ebx
	xor eax,eax
	xor ebx,ebx

	push eax 	; Push \x00 terminator into the stack
	push 0x68732f2f ; Push //sh to the stack
	push 0x6e69622f ; Push /bin to the stack

	; execve("/bin/sh",0,0)
	mov al,0xb	; Syscall for execve
	mov ebx,esp	; "/bin/sh"
	xor ecx,ecx	; 0x0
	xor edx,edx	; 0x0
	int 0x80	; Calls kernel	

section .data
	message: db "We are going to pop a shell! "
	mlen equ $-message
