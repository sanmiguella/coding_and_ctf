global _start

section .text

_start:
    jmp Begin

NeverExecute:
    mov rax, 0x10
    xor rbx, rbx

Begin:
    mov rax, 0x5        ; Max amount of times message will be printed to console

PrintHW:
    push rax            ; Push the current value of rax into the stack

    ; Print onscreen
    mov rax, 1          ; Syscall for write()
    mov rdi, 1          ; Arg 1 - File Descriptor - Stdout
    mov rsi, message    ; Arg2 - Message to be displayed
    mov rdx, mlen       ; Arg3 - Length of message
    syscall             ; Calls kernel 

    pop rax             ; Stores the value at the top of the stack into the rax register
    dec rax             ; Decrements the current rax value by 1
    jnz PrintHW         ; Loops if zero flag isn't set

Exit:
    mov rax, 60         ; Syscall for exit()
    mov rdi, 11         ; Exit code
    syscall

section .data
    message: db "Hello world! ", 0x0A
    mlen equ $-message
