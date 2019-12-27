section .data
    MorningGreeting: db "Good morning",0xa 
    morningGreetingLen equ $-MorningGreeting

    NightGreeting: db "Good night",0xa
    nightGreetingLen equ $-NightGreeting
    
section .text
    global _start

_start:
    mov cl,0x5 ; Max times morning greeting will loop
    jmp Day    ; Jumps to morning greeting

Day:
    push ecx    ; Saves current value of counter in stack
        
    mov al,0x4  ; Syscall # for write 
    mov bl,0x1  ; File descriptor - STDOUT
    mov ecx,MorningGreeting     ; Pointer to morning greeting message
    mov dx,morningGreetingLen   ; Morning greeting message length
    int 0x80                    ; Calls kernel

    pop ecx     ; Restores the current loop iteration from stack to register
    loop Day    ; Decrements loop counter by 1 and if it is 0, stops looping 

    mov cl,0x4  ; Max times night greeting will loop
    jmp Night   ; Jumps to night greeting subroutine

Night:
    push ecx    ; Saves current value of counter in stack
    
    mov al,0x4  ; Syscall # for write
    mov bl,0x1  ; File descriptor - STDOUT
    mov ecx,NightGreeting       ; Pointer to night greeting message
    mov dx,nightGreetingLen     ; Night greeting message length
    int 0x80    ; Calls kernel

    pop ecx     ; Restores the current loop iteration from stack to register
    loop Night  ; Decrements loop counter by 1 and if it is 0, stops looping

    jmp ExitProgram ;Jumps to exit subroutine

ExitProgram:
    mov al,0x1      ; Syscall # for exit
    xor ebx,ebx     ; Exit code
    int 0x80        ; Calls kernel
