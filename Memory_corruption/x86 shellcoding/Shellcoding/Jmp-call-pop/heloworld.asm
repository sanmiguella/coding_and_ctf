global _start

section .text

_start:
    jmp short call_helloworld

print_helloworld:
    xor eax, eax 
    xor ebx, ebx
    xor ecx, ecx
    xor edx, edx
   
    ; print `hello world` to console 
    mov al, 0x4     ; syscall # for write()
    mov bl, 0x1     ; FD - stdout
   
    pop ecx             ; ecx - hello world
    mov dl, output_len  ; dl - length of hello world
    int 0x80            ; Calls kernel

    jmp short call_binSH

print_binSH:
    ; print `/bin/sh` to console
    mov al, 0x4     ; syscall # for write()
    mov bl, 0x1     ; FD - stdout

    pop ecx             ; ecx - /bin/sh
    mov dl, binSH_len   ; dl - length of /bin/sh
    int 0x80            ; Calls kernel

    jmp short call_cmd

popShell:
    ; execve('/bin/sh', 0, 0)
    ; after jmp, '/bin/sh' will be on the stack, mov ebx, &addr will not work
    ; pop ebx will put the value of '/bin/sh' into ebx
    mov al, 0xB     ; syscall # for execve
    pop ebx         ; ebx - /bin/sh

    xor ecx, ecx    ; ecx - 0
    xor edx, edx    ; edx - 0

    int 0x80        ; Calls kernel

exit:
    xor eax, eax
    mov al, 0x1     ; syscall # for exit()

    xor ebx, ebx
    mov bl, 0xFF    ; exit code

    int 0x80        ; Calls kernel

call_helloworld:
    call print_helloworld

    output: db "hello world", 0xD, 0xA
    output_len equ $-output

call_binSH:
    call print_binSH

    binSH: db "/bin/sh", 0xD, 0xA
    binSH_len equ $-binSH

call_cmd:
    call popShell

    cmd: db "/bin/sh", 0x00
    
