global _start

section .text

; execve("/bin//sh",["/bin//sh",0],0)
_start:
    xor rax, rax 
    xor rdx, rdx    ; 3rd arg, rdx = 0
  
    ; [ /bin//sh | null ] 
    push rax        ; For null terminator
    push rax        ; For /bin//sh
    mov dword[rsp], "/bin"
    mov dword[rsp +4], "//sh"

    ; [ ptr to /bin//sh | null | /bin//sh | null ]
    mov rdi, rsp    ; 1st arg, rdi = /bin//sh
    push rax        ; For null terminator
    push rdi        ; For ptr to /bin//sh   
    mov rsi, rsp    ; 2nd arg, rsi = ptr to /bin//sh
 
    add al, 59      ; Syscall number for execve()
    syscall
