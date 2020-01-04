section .text
    global _start

_start:
    ; Zero-ing eax/ebx/ecx/edx registers
    xor eax, eax
    xor ebx, ebx
    xor ecx, ecx
    xor edx, edx

str_formation:
                        ; Stack layout
    push eax            ; 0x00
    push 0xD            ; \r\x00
    push 0xA            ; \n\r\x00
    push 0x002E2E2E     ; ...\n\r\x00
    push 0x29287469     ; it()...\n\r\x00
    push 0x78652067     ; g exit()..\n\r\x00
    push 0x6E697475     ; uting exit()..\n\r\x00
    push 0x63657845     ; Executing exit()..\n\r\x00

print:
    mov al, 0x4             ; Syscall #nbr for write()
    mov bl, 0x1             ; FD - Stdout
    mov ecx, esp            ; String to be printed
    mov dl, 0x13            ; Length of string to be printed
    int 0x80                ; Calls kernel

exit:
    xor eax, eax            ; eax = 0
    inc eax                 ; eax = 1, sycall #nbr for exit()
    xor ebx, ebx            ; ebx = 0 
    mov bl, 0xFF            ; bl = 255 , exit code
    int 0x80                ; Calls kernel
