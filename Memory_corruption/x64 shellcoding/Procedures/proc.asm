global _start

section .text

hello_world_proc:
    mov rax, 1              ; Syscall number for write()
    mov rdi, 1              ; 1st arg - stdout
    mov rsi, hello_world    ; 2nd arg - message to display
    mov rdx, length         ; 3rd arg - message length
    syscall                 ; Calls kernel
    ret                     ; signifies end of procedure

_start:
    mov rcx, 5

print_hello_world:
    push rcx                ; Save current loop counter to stack
    call hello_world_proc   ; Calls the subroutine that prints message to the console
    pop rcx                 ; Pops the current loop counter value to register
    loop print_hello_world  ; rcx will automatically be decremented on each loop iteration until rcx reaches 0 and loop terminates
    
exit:
    ; Graceful exit 
    mov rax, 60             ; Syscall number for exit()
    xor rdi, rdi            ; 1st arg - exit code(0)
    syscall                 ; Calls kernel

section .data
    hello_world: db "Hello world!", 0x0A 
    length equ $-hello_world
