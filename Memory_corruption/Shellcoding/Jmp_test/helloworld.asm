global _start

section .text

_start:
    jmp two ; Jumps to label - two

one:
    ; Zeroing of eax and ebx register
    xor eax, eax
    xor ebx, ebx

    mov al, 0x4             ; Syscall # for write()
    mov bl, 0x1             ; STDOUT
    mov ecx, [esp]          ; [esp] = '/etc/passwd'
    mov dl, filename_len    ; length of '/etc/passwd' 
    int 0x80                ; Calls kernel

exit:
    ; If there are no zeroing of registers, program will bug out when
    ; its integrated with C 
    xor eax, eax            
    xor ebx, ebx

    mov al, 0x1             ; Syscall # for exit()
    mov bl, 0xFF            ; exit code 255
    int 0x80                ; Calls kernel

two:
    call one    ; When it jumps to one, esp will point to "/etc/passwd"
    filename: db "/etc/passwd" 
    filename_len equ $-filename 
