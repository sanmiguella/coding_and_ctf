global _start

section .text

_start:
    mov rax, 0x00000000FFFFFFFF 
    sal rax, 32	; Shift left 32 bits -> 0xFFFF FFFF 0000 0000
    sal rax, 1	; Shift left 1 bit -> 0xF -> 1111 -> (shift left 1 bit) -> 1110 -> 0xE -> 0xFFFF FFFE 0000 0000 with CF(carry flag) set

    clc		; Clear carry
    mov rax, 0x00000000FFFFFFFF
    shr rax, 1 	; Shift right 1 bit -> 0xF -> 1111 -> (shift right 1 bit) -> 0111 -> 0x7 -> 0x0000 0000 7FFF FFFF with CF(carry flag) set
    shr rax, 31	; Shift right 31 bits -> 0x7 -> 0111 -> 0x7FFF FFFF -> 3 + 28 = 31 bits -> (shift right 31 bits) -> 0x0000 0000 0000 0000

    clc		; Clear carry
    mov rax, 0x00000000FFFFFFFF	
    sar rax, 1	; Shift arithmetic right 1 bit -> 0xF -> 1111 -> positive operand(sar) -> 0111 -> 0x7 -> 0x0000 0000 7FFF FFFF with CF(carry flag) set
    clc		; Clear carry
    mov rax, 0xFFFFFFFFFFFFFFFF
    sar rax, 1	; Shift arithmetic right 1 bit -> 0xF -> 1111 -> negative operand(sar) -> 1111 -> 0xF -> 0xFFFF FFFF FFFF FFFF with CF(carry flag) & SF(sign flag) set

    clc
    mov rax, 0x0123456789abcdef
    ror rax, 8	; Rotate by 1 byte -> ef0123456789abcd
    ror rax, 12	; Rotate by 1.5 byte -> bcdef0123456789a
    ror rax , 44 ; Rotate by 5.5 bytes -> 0123456789abcdef -> back to original sequence as 44 + 12 = 64 bits

exit:
    ; Graceful exit
    mov rax, 0x3C
    mov rdi, 0
    syscall

section .data
    var1 dq 0x1111111111111111
    var2 dq 0x0 
