.386
.model flat, c ; Use C language style names for public symbols
.code

; Return : 0 Error(Division by 0)
;		   1 Success
; 
; Computation *prod = a * b
;			  *quo = a / b
;			  *rem = a % b

integer_mul_div proc
	; Function prologue
	push ebp
	mov ebp, esp 
	
	; CPP calling conventions
	; Must preserve the value of - ebx, esi, edi, ebp : non-volatile registers
	;							   eax, ecx, edx : volatile registers
	push ebx
	xor eax, eax ; Attempting to make sure divisor is not equal to 0

	mov ecx, [ebp +8] ; ecx = 'a' 
	mov edx, [ebp +12] ; edx = 'b' 

	; Bitwise or edx with itself to update the status flags in the E flags register while preserving 
	; the original value in register edx
	; TLDR: testing the argument 'b' to avoid division by zero condition
	or edx, edx	

	; jz - jump if zero
	; Conditional jump instruction that gets performed only if the Zero flag in the Eflag register
	; is set to 1 or is True
	jz invalid_divisor 

	imul edx, ecx ; edx = 'b' * 'a'

	mov ebx, [ebp +16] ; ebx = 'prod'
	mov [ebx], edx ; Saves 'prod'

	; Calculate the remainder and quotient 
	mov eax, ecx ; eax = 'a' 
	cdq  ; edx: eax contains dividend

	; Performs signed integer division
	; Content of register pair edx, eax is always used as dividend
	idiv dword ptr[ebp +12] ; [ebp +12] : address of 'b'

	; After performing the division registers eax and edx contains quotient and remainder

	; eax: quotient
	mov ebx, [ebp +20] ; [ebp +20] : address of 'quo'
	mov [ebx], eax ; Saves the quotient

	; edx: remainder
	mov ebx, [ebp +24] ; [ebp +24] : address of 'rem'
	mov [ebx], edx ; Saves the remainder

	mov eax, 1 ; Return value : Successfully done the work

	; If our functions used a non-volatile register, a program crash may occur
	invalid_divisor:
		; Function epilogue
		pop ebx
		pop ebp
		ret

integer_mul_div endp
end