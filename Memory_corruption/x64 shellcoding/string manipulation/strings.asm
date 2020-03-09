global _start

section .text

_start:
    ; Movs b/w/d/q
    ; Memory to memory
    cld					; Clear directional flag
    lea rsi, [HelloWorld]		; Load address of HelloWorld variable into rsi
    lea rdi, [Dest]			; Load address of Dest variable into rdi
    movsq				; Moves 64 bits, qword, 8 bytes, 8 chars
    ;movsd				; Moves 32 bits, dword, 4 bytes, 4 chars
    ;movsw				; Moves 16 bits,  word, 2 bytes, 2 char
    ;movsb				; Moves 8 bits, 1 byte

    cld
    lea rsi, [HelloWorld]		; Source string to be copied from
    xor rax, rax			; Zeroes rax register
    mov qword [Dest], rax		; Zeroes values in Dest variable
    lea rdi, [Dest] 			; Destination string to be copied to
    mov rcx, len			; Length of the string to be copied
    rep movsb				; Copies string one byte at a time till the end of the string is reached

    ; stos b/w/d/q
    ; Register to memory
    mov rax, 0x0123456789abcdef		; Moves value to rax register
    lea rdi, [var1]			; Load the address of var1 variable into rdi register
    stosq				; Moves value from rax register to variable var1

exit:
    mov rax, 60		; Syscall for exit()
    mov rdi, 0		; Exit code number
    syscall		; Calls kernel

section .data
    HelloWorld: db "Hello World"	; Message to be printed
    len equ $-HelloWorld		; Length of HelloWorld string

section .bss
    Dest: resb len			; To reserve space according to the length of HelloWorld
    var1: resb 8			; Reserve 8 bytes
    
