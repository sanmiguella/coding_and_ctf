global _start

section .data 
    greeting: db `hello world!\n`
    greetingLen equ $-greeting
    
    binSH: db "/bin/sh" 

section .text

HelloWorldProc:
    ; Prologue
    ; Storing current frame pointer into the stack
    ; and moving the value of esp into ebp
    push ebp 
    mov ebp,esp 
    
    ; Print hello world using write syscall
    mov al,0x4  ; Syscall # for write()
    mov bl,0x1  ; FD - stdout
    mov ecx,greeting    ; Message to be displayed to the console
    mov dl,greetingLen  ; Message length
    int 0x80            ; Calls the kernel

    ; Epilogue
    ; Move the value of ebp into esp and pop ebp
    ; Below 2 instructions is the same as leave
    ; mov esp,ebp 
    ; pop ebp
    leave
    ret     ; Signifies the end of the procedure

_start:
    mov ecx,0x4 ; Max value of Loop

PrintHelloWorld:
    ; Preserves registers and flags
    pushad
    pushfd

    call HelloWorldProc ; Calls the helloworld procedure
    
    ; Restores registers and flags 
    popfd
    popad
   
    ; If ecx is not 0, loop continues 
    loop PrintHelloWorld

PopShellProc:
    ; Prologue
    ; Storing current frame pointer into the stack
    ; and moving the value of esp into ebp
    push ebp
    mov ebp,esp 

    mov al,0xb
    mov ebx,binSH
    xor ecx,ecx
    xor edx,edx
    int 0x80  

    ; Epilogue
    ; Move the value of ebp into esp and pop ebp
    ; Below 2 instructions is the same as leave
    ; mov esp,ebp 
    ; pop ebp
    leave
    ret

PopShell:
    ; Preserves registers and flags
    pushad
    pushfd
    
    call PopShellProc ; Calls the popshell procedure

    ; Restores registers and flags
    popfd
    popad

Exit:
    xor eax,eax     ; Zeroes ecx
    inc eax         ; eax = 1, syscall # for exit
    xor ebx,ebx     ; exit code
    int 0x80        ; Calls the kernel
