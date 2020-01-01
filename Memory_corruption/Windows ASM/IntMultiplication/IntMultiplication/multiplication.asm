.386
.model flat, c
.code 

multiply_asm proc 

; Prologue 
push ebp
mov ebp, esp 

; int multiply_asm(int a, int b);
xor eax, eax 
xor ecx, ecx 

mov eax, [ebp + 8]	; eax = a
mov ecx, [ebp + 12] ; ecx = b
imul eax, ecx		; eax = a  * b

pop ebp 
ret 

multiply_asm endp 
end 