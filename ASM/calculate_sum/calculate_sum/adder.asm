.386
.model flat, c	; C style names for public symbols
.code 

adder_ASM proc	; Create procedure
	
	; Function Prolog
	; Initialize/Create stack frame
	push ebp		; Save the content of EBP into the stack / Saves value of calling function, Decrement ESP
	mov ebp, esp	; Copies the content of ESP to EBP, EBP - base pointer register, ESP - stack pointer register

	; Arguments
	; ebp +4 = return address
	mov eax, [ebp +8]  ; eax = argument A
	mov ecx, [ebp +12] ; ebx = argument B
	mov edx, [ebp +16] ; edx = argument C 

	; Performing Addition
	add eax, ecx ; eax = A + B
	add eax, edx ; eax = A + B (From earlier addition) + C

	; x86 must use EAX to return 32 bit integer value to calling function, that is why results are stored in EAX
	; Function Epilogue
	pop ebp ; To restore calling function value, Increment ESP 
	ret  ; Transfer control back to the calling function

adder_ASM endp 
end


