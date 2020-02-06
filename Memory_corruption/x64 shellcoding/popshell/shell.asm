global _start

section .data

_start:
    ; Zero-ing of registers rax-rcx & rsi-rdi
    xor rax, rax
    xor rbx, rbx

    xor rdi, rdi
    xor rsi, rsi

    jmp short call_shell

; RAX - Syscall, RDI - 1st arg, RSI - 2nd arg, RDX, 3rd arg
; execve(const char *filename, const char *const argv[], const char *const envp[])

shell:
    mov rdi, [rsp]	; 1st ARG - "/bin//sh"
    xor rdx, rdx	; 3rd ARG - NULL 
    
    mov rbx, rsp	; RBX - Pointer to stack address whose value points to location of "/bin//sh" 

    ; [ ptr to "/bin//sh" | NULL | "/bin//sh" ]
    push rdx		
    push rbx	
    
    mov rsi, rsp	; 2nd ARG - ptr to "/bin//sh"
    add rax, 59		; Syscall # for execve()
    syscall

call_shell:
    call shell
    binSH: db "/bin//sh"
