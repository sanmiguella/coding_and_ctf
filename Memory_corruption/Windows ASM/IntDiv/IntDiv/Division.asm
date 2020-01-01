.386
.model flat, c
.code

integer_division_asm proc

	; prologue
	push ebp 
	mov ebp, esp 

	; saving of registers
	push ebx

	; division_asm(int a, int b, int quotient, int remainder);
	; a = [ebp + 8]
	; b = [ebp + 12]
	; quotient = [ebp + 16]
	; remainder = [ebp + 20]
	xor eax, eax 
	xor ebx, ebx
	xor ecx, ecx 

	; make sure the divisor is not 0
	mov ecx, [ebp + 8] ; ecx = a
	mov edx, [ebp + 12] ; edx = b
	or edx, edx 
	jz Exit ; jump if zero into exit

	mov eax, ecx ; eax = a
	cdq	; edx:eax = dividend(a)

	; divided by 'b', b : 4 bytes, double word : 4 bytes
	idiv dword ptr[ebp + 12] ; eax = quotient , edx = remainder

	; move values into the appropriate variables
	mov ebx, [ebp + 16] ; ebx = quotient
	mov [ebx], eax ; save quotient

	mov ebx, [ebp + 20] ; ebx = remainder
	mov [ebx], edx ; save remainder

	; epilogue
	Exit:
	pop ebx
	pop ebp
	ret

integer_division_asm endp
end