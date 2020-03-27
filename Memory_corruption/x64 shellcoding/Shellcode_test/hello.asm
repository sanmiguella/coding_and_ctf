global _start

section .text

_start:
    ; Zero-ing of registers
    xor rax, rax    
    xor rcx, rcx

    xor rdi, rdi
    xor rsi, rsi
    xor rdx, rdx

    ; jmp-call-pop technique to include the address of "hello world" string into the stack
    jmp short greeting

printGreeting:
    pop rsi                 ; For copying of string using rep movsb, rsi will be the source string, in this case, it will be the defined string
   
    push rax                ; Pushing of null terminator to prepare space in the stack for the "hello world" string
    push rax 
    
    lea rdi, [rsp]          ; For copying of string using rep movsb, rdi will be the dest string, in this case, it will be in the stack
    mov cl, hello_len       ; Length of string to be copied
    rep movsb               ; Byte by byte copying until the desired string length is reached. On every loop rcx is decremented by 1 until rcx is 0.

    add al, 1               ; rax = 1 , syscall write()
    xor rdi, rdi            ; rdi = 0 
    add dil, 1              ; rdi = 1 , stdout
    mov rsi, rsp            ; rsi = "hello world"
    mov dl, hello_len       ; rdx = lenth of hello world
    syscall                 ; Calls kernel
    
exit:
    xor rax, rax    ; rax = 0
    add al, 60      ; rax = 60 , syscall exit()
    xor rdi, rdi    ; rdi = 0 , exit code = 0
    syscall         ; Calls kernel

greeting:
    call printGreeting  ; Will push the address of next instruction into the stack, next instruction -> hello: db "hello world", 0xA

    hello: db "hello world", 0xA
    hello_len equ $-hello
