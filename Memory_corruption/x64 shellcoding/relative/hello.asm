global _start
default rel         ; To use relative addressing so there isn't any need to : lea rsi, [rel hello_world]

section .text

_start:
    ; Print on screen
    xor rax, rax    ; Clear register
    
    add rax, 1      ; Syscall for write()
    mov rdi, rax    ; 1st arg: stdout
    lea rsi, [hello_world]  ; 2nd arg: msg to be printed
    
    xor rdx, rdx    ; Clear register
    add rdx, 12     ; 3rd arg: length of msg to be printed     
    syscall         

    ; Graceful exit
    xor rax, rax    ; Clear register
    add rax, 60     ; Syscall for exit()
    xor rdi, rdi    ; Clear register, exit code(0)
    syscall

    hello_world: db 'hello world', 0xA
