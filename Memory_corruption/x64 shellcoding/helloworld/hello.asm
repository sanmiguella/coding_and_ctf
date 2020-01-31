global _start

section .text
_start:
    ; Zeroing of registers rax to rdx
    xor rax, rax
    xor rbx, rbx
    xor rcx, rcx
    xor rdx, rdx  

    jmp short call_greetUser    ; jmp-call-pop

; write()
greetUser:
    ; rdi(1st), rsi(2nd), rdx(3rd), r10(4th), r8(5th), r9(6th)
    mov al, 1                   ; Syscall number for write()
    mov dil, 1                  ; rdi: 1(stdout)
    pop rsi                     ; String to write to stdout
    mov dl, greetingLen         ; rdx: Length of greeting string

    syscall                     ; x64 equivalent of int 0x80

; exit()
exit:
    xor rax, rax                ; Zeroes rax register
    add al, 60                  ; Syscall number for exit()

    xor rdi, rdi                ; Zeroes rbx register
    add dil, 255                ; rdi: 255(exit code)

    syscall                     ; x64 equivalent of int 0x80

call_greetUser:
    call greetUser              ; When call is used the value of the next instruction is saved on the stack

    ; db -> define byte
    greeting: db `hello world\n`
    greetingLen equ $-greeting
