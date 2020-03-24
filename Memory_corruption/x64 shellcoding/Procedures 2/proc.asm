global _start

section .text

hello_world_proc:
    ; Print hello world using write syscall
    mov rax, 1  ; Syscall for write()
    mov rdi, 1  ; Stdout
    mov rsi, hello_world    ; Message to be displayed
    mov rdx, length ; String length
    syscall ; Calls kernel

    ret ; Signifies the end of procedure, instructio pointer will load the next instruction which is pop rcx

_start:
    mov rcx, 0x3    ; To loop 3 times, rcx is used as a counter
    
print_hello_world:
    push rcx    ; Save current count value to the stack
    call hello_world_proc    ; Calls function to write data to the screen, address of pop rcx is saved into the stack
    pop rcx ; Transfer data from stack to memory for the purpose of decrementing it
    loop print_hello_world ; Will loop unless rcx is 0

exit:
    mov rax, 60 ; Syscall for exit()
    mov rdi, 11 ; exit code
    syscall ; Calls kernel

section .data
    hello_world: db "Hello world!", 0x0A
    length equ $-hello_world
