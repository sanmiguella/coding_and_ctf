global _start

section .text

_start:
    mov rcx, 5          ; The amount of time print will loop

print:
    push rcx            ; Push the current rcx value to the stack

    ; Write data to console
    mov rax, 1          ; Syscall for write()
    mov rdi, 1          ; 1st arg: stdout
    mov rsi, message    ; 2nd arg: Message to be printed
    mov rdx, len        ; 3rd arg: Length of message
    syscall             ; Calls kernel

    pop rcx             ; Pops the value from the stack to rcx register
    loop print          ; loop instruction will decrement rcx register by 1
   
exit:
    mov rax, 60         ; Syscall for exit()
    mov rdi, 1          ; 1st arg: exit code
    syscall             ; Calls kernel

section .data
    message: db "hello world", 0x0A ; 0x0A : newline, "hello world" will be stored in message variable
    len equ $-message               ; Length of message will be stored in len variable
