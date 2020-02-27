global _start

section .text

_start:
    ;NOT operation
    mov rax, qword[var2]	; rax: 0x0 
    not rax			; rax: 0xFFFF FFFF FFFF FFFF

    mov rbx, qword[var1]	; rax: 0x1111 1111 1111 1111 , 0x1: 0001
    not rbx			; (not) 0001 : 1110 -> E , (not) 0x1111 1111 1111 1111 -> 0xEEEE EEEE EEEE EEEE
    
    ; AND operation
    mov rax, qword[var2]	; rax: 0x0
    mov rbx, qword[var1]	; rbx: 0x1111 1111 1111 1111 , 0x1: 0001
    and rbx, rax		; 0001 (and) 0000 -> 0000 , 0x0000 0000 0000 0000 (and) 0x1111 1111 1111 1111 -> 0x0000 0000 0000 0000 

    mov rbx, qword[var1]	; rbx: 0x1111 1111 1111 1111
    and rbx, qword[var1]	; 0x1: 0001 , 0001 (and) 0001 -> 0001, 0x1111 1111 1111 1111 (and) 0x1111 1111 1111 1111 -> 0x1111 1111 1111 1111
    
    ; OR operation
    mov rax, qword[var2]	; rax: 0x0 
    mov rbx, qword[var1]	; rbx: 0x1111 1111 1111 1111 , 0x1: 0001
    or rbx, rax			; 0001 (or) 0000 -> 0001 -> 0x1, 0x0000 0000 0000 0000 (or) 0x1111 1111 1111 1111 -> 0x1111 1111 1111 1111
    
    mov rbx, qword[var1]	; rbx: 0x1111 1111 1111 1111 , 0x1: 0001
    or rbx, qword[var1]		; 0001 (or) 0001 -> 0001 ,0x1111 1111 1111 1111 (or) 0x1111 1111 1111 1111 -> 0x1111 1111 1111 1111

    ; XOR operation
    mov rax, 0x0101010101010101	; rax: 0x0101010101010101	
    mov rbx, 0x1010101010101010 ; rbx: 0x1010101010101010
    xor rax, rbx		; rax: 0x1111111111111111

    xor rax, rax		; 0x1111 1111 1111 1111 (XOR) 0x1111 1111 1111 1111 = 0x0

    xor qword[var1], rax	; 0x1111 1111 1111 1111 (XOR) 0x0000 0000 0000 0000 = 0x1111 1111 1111 1111

exit:
    ; Graceful Exit
    mov rax, 0x3C
    mov rdi, 0
    syscall

section .data
    var1 dq 0x1111111111111111
    var2 dq 0x0
