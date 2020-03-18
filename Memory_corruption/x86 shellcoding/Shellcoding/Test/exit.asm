global _start

section .text
_start:
    ; Zero-ing of registers ebx,ecx,edx
    xor ebx, ebx
    xor ecx, ecx
    xor edx, edx
   
    ; No '\x00' and '\x0A' 
    xor eax, eax    ; eax = 0x00
    push eax        ; stack = "\x00"

    mov al, 0x9     ; eax = 0x9
    inc eax         ; eax = 0xA
    push eax        ; stack = "\x0A\x00"
    push 0x21216f6f ; stack = "oo!!\x0A\x00" 
    push 0x6c6c6568 ; stack = "helloo!!\x0A\x00"
    mov ecx, esp    ; ecx = "helloo!!\x0A\x00"

    mov al, 0x4         ; Syscall # for write()
    mov bl, 0x1         ; FD - STDOUT
    mov dl, 0x8         ; Char length = 8
    int 0x80            ; Calls kernel

    mov al, 0x1         ; Syscall # for exit()
    mov bl, 0xF         ; Exit code
    int 0x80            ; Calls the kernel
