extern printf
extern gets

global main

section .text
main:
    ; printf("Please enter data:\n")
    push getInput       ; Push data to be printed to the stack
    call printf         ; Calls printf()
    add esp, 0x4        ; Same as popping 1 argument off the stack

    ; gets(buffer)
    lea edi, [buffer]   ; Load address of buffer in edi
    push edi            ; Put the address of edi into the stack
    call gets           ; Call gets()
    add esp, 0x4        ; Same as popping 1 argument off the stack

    ; printf("\nResults:\n")
    push showResults    ; Push address of showResults to be printed to the stack
    call printf         ; Calls printf()
    add esp, 0x4        ; Same as popping 1 argument off the stack

    ; printf(buffer)
    push edi           ; Push address of edi into the stack
    call printf        ; Calls printf()
    add esp, 0x4       ; Same as popping 1 argument off the stack

    push newLines      ; Push address of newLines into the stack
    call printf        ; Calls printf()
    add esp, 0x4       ; Same as popping 1 argument off the stack

section .data
    ; Variables section
    ; 0xA -> newline, 0x00 -> Null terminator
    getInput: db `Please enter data:\n\x00` ; Newline and null terminator as printf() will stop printing upon encountering \x00
    showResults: db `\nResults:\n\x00`
    newLines: db `\n\x00`

section .bss
    ; char buffer[128]
    buffer: resb 128    ; Reserves 128 bytes of buffer
