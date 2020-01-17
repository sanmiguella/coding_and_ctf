global _start

section .text

_start:
    ; Zeroes registers eax to edx
    xor eax, eax
    xor ebx, ebx
    xor ecx, ecx
    xor edx, edx

    ; REMEMBER for any commands or arguments, words must be multiples of 4
    ; /bin//sh -> 8   
    ; /etc//passwd -> 12
    push eax        ; NULL
    push "/cat"
    push "/bin"
    mov ebx, esp    ; ebx - /bin/cat\x00
  
    push eax        ; NULL 
    push "sswd"
    push "//pa"
    push "/etc"
    mov esi, esp    ; esi - /etc/passwd\x00
    
    push eax        ; NULL
    push esi        ; Address of /etc//passwd\x00
    push ebx        ; Address of /bin/cat\x00 

    mov ecx, esp    ; ["/bin/cat","/etc//passwd"]
    
    mov al, 0xB     ; Syscall # for execve()
    int 0x80        ; Calls kernel

exit:
    xor eax, eax    
    mov al, 0x1     ; Syscall # for exit()

    xor ebx, ebx    ; Exit code

    int 0x80        ; Calls kernel
