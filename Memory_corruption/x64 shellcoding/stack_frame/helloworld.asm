global _start

section .text

hello_world_proc:
    push rbp
    mov rbp, rsp

    ; Print hello world using write() syscall
    mov rax, 1  ; Syscall number for write()
    mov rdi, 1  ; FD - stdout
    mov rsi, hello_world    ; Message to be displayed
    mov rdx, length ; Length of message to be displayed
    syscall     ; Calls kernel

    ;mov rsp, rbp
    ;pop rbp

    leave   

    ret ; Signifies end of procedure

_start:
    mov rcx, 3  ; To print hello world 3 times, rcx is a counter

print_hello_world:
    push rcx    ; Saves current counter value to the stack
    call hello_world_proc   ; Calls the routine to print messages to the console
    pop rcx     ; Moves the current counter value from stack to register to allow loop to decrement it
    loop print_hello_world  ; Loop continues until rcx is 0

exit:
    mov rax, 60 ; Syscall number for exit()
    mov rdi, 11 ; Exit code
    syscall     ; Calls kernel

section .data
    hello_world: db "hello world!", 0x0A
    length equ $-hello_world
