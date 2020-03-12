global _start

section .text

_start:
    ; Display prompt
    mov al, 1               ; Syscall for write()  
    mov dil, 1              ; rdi - 1 , stdout
    mov rsi, prompt         ; rsi - string to be displayed
    mov dl, prompt_len      ; rdx - string length
    syscall
   
    ; Get input 
    xor rax, rax            ; Syscall for read()

    ; [ 8 byte buffer | null ]
    push rax                ; For null terminator
    push rax                ; For buffer

    lea rsi, [rsp]          ; rsi will contain address of buffer
    mov dl, 8               ; Only read 8 bytes 
    syscall

    cld                     ; Clear directional flag
    pop rax                 ; Pop the password that has been entered off the stack and into rax
    lea rdi, [password]     ; Loads address of the password string to be compared
    scasq                   ; Compares rax to rdi, compares register to memory

    jne failed              ; If password isnt identical to one in memory, ZF isnt set

passed:
    xor rax, rax            
    add  al, 1              ; Syscall for write()
    mov rdi, 1              ; STDOUT
    mov rsi, pass           ; String to be displayed
    mov rdx, pass_len       ; String length
    syscall
    
    jmp short exit          ; Jump to exit label    

failed:
    xor rax, rax        
    add al, 1               ; Syscall for write()
    mov rdi, 1              ; STDOUT
    mov rsi, fail           ; String to be displayed
    mov rdx, fail_len       ; String length
    syscall

exit:
    xor rax, rax             
    add al, 60              ; Syscall for exit
    xor rdi, rdi            ; rdi - Exit code
    syscall

section .data
    password: dq "password",0x0

    prompt: dq "Pass:"
    prompt_len equ $-prompt

    pass: dq "Passed", 0x0, 0xa
    pass_len equ $-pass

    fail: dq "Failed", 0x0, 0xa
    fail_len equ $-fail
