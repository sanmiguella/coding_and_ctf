global _start

section .text

_start:
    xor rax, rax    ; Zeroes rax register
    mov al, 0x1     ; Moves value of 0x1 into rax

    xor rbx, rbx    ; Zeroes rbx register
    mov bl, 0x2     ; Moves value of 0x2 into rbx

    xor rcx, rcx    ; Zeroes rcx register
    mov cl, 0x3     ; Moves value of 0x3 into rcx
    
    xor rdx, rdx    ; Zeroes rdx register
    mov dl, 0x4     ; Moves value of 0x4 into rdx

exit:
    mov al, 60      ; Decimal 60, Syscall number for exit x64
    xor rdi, rdi    ; Zeroes rdi register

    mov di,0xFFFF   ; If rdi is 0xFF there are null chars      
    
    syscall         ; 64 bit version of int 0x80
