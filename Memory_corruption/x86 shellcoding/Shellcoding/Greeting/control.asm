section .data
	greeting: db "hello world",0xa ; Greeting message for user
	mlen equ $-greeting	       ; For use with write() later

	binSH: db "/bin/sh" ; Command for execve() 

section .text
	global _start

_start:
	mov al,0x2    ; Maximmum loop value
	jmp GreetUser ; Jumps to GreetUser subroutine 

GreetUser:
	push eax	 ; Saves the current loop value to the stack

	mov al,0x4	 ; Syscall # for write
	mov bl,0x1	 ; #1 means STDOUT
	mov ecx,greeting ; Pointer to string containing hello world
	mov dl,mlen 	 ; Length of the message to be displayed
	int 0x80	 ; Calls kernel

	pop eax		 ; Pop the current loop value from the stack to eax
	dec eax		 ; Decrements the current loop value by 1
	test eax,eax	 ; Checks if eax is 0
	jnz GreetUser	 ; If zero flag isn't set aka loop value isnt 0, GreetUser

PopShell:
	; Zeroes the eax to edx register
	xor eax,eax
	xor ebx,ebx
	xor ecx,ecx	
	xor edx,edx

	; execve("/bin/sh",0,0)
	mov al,0xb	; Syscall # for execve
	mov ebx,binSH	; "/bin/sh"
	int 0x80	; Calls kernel

Exit:
	; Having an exit() is necessary, else program will segfault
	; Zeroes eax,ebx register
	xor eax,eax	
	xor ebx,ebx

	; exit(0)	
	mov al,0x1 ; Syscall # for exit
	int 0x80   ; Calls kernel
