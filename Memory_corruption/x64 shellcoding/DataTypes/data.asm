global _start

section .text

_start:

        ; print on screen

        mov rax, 1
        mov rdi, 1
        mov rsi, hello_world
        mov rdx, length
        syscall

	xor rax, rax
	mov ax, [var1]

	xor rax, rax
	mov ax, [var2]

	xor rax, rax
	mov eax, [var3] 

	xor rax, rax
	mov rax, [var4]    

	xor rax, rax
	mov rax, repeat_buffer

        ; exit gracefully

        mov rax, 60
        mov rdi, 11
        syscall

section .data

        hello_world: db 'Hello World to the SLAE-64 Course',0xa
        length: equ $-hello_world

        var1: db 0x11, 0x22		; Define byte
        var2: dw 0x3344			; Define word
        var3: dd 0xaabbccdd		; Define dword
        var4: dq 0xaabbccdd11223344	; Define qword

        repeat_buffer: times 123 db 0x41

section .bss
        buffer: resb 64
