global _start

section .text
_start:
    ; register based addition
    mov rax, 0x1
    add rax, 0x1

    mov rax, 0xFFFFFFFFFFFFFFFF
    add rax, 0x1
    
    mov rax, 0x9
    sub rax, 0x4    
    
    ; memory based addition
    mov rax, qword [var1]   ; rax : 0x1
    add qword[var4], rax    ; var4 : 0x1
    
    add qword[var4], 0x2    ; var4 : 0x3

    ; clear / set / complement carry flag
    clc ; Clear carry flag
    stc ; Set carry flag
    cmc ; Complement carry flag

    ; add with carry
    mov rax, 0 
    stc             ; set carry

    adc rax, 0x1    ; (adc : add with carry) -> 0x0(rax) + 0x1(value to be added) + 0x1(carry flag) = 0x2
    stc             

    adc rax, 0x2    ; 0x2(rax) + 0x2(value to be added) + 0x1(carry flag) = 0x5

    ; subtract with borrow
    mov rax, 0x10
    sub rax, 0x5    ; 0x10 - 0x5 = 0xB(11)
    stc             
    sbb rax, 0x4    ; (sbb : subtract with borrow) -> 0xB - 0x4(value to be subtracted) - 0x1(carry flag) = 0x6

    ; increment and decrement
    inc rax         ; increment rax by 1
    dec rax         ; decrement rax by 1 

    ; exit the program gracefully
    mov rax, 0x3C   ; Syscall number for exit()
    mov rdi, 0      ; Exit code
    syscall         ; Calls kernel

section .data
    var1    dq  0x1
    var2    dq  0x1122334455667788
    var3    dq  0xFFFFFFFFFFFFFFFF
    var4    dq  0x0
