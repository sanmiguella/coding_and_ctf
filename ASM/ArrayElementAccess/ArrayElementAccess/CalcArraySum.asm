.model flat, c
.code 

; CalcArraySumASM(int *x, int n)
CalcArraySumASM proc
	push ebp			; Prologue
	mov ebp, esp 

	; [ebp + 8]	 -> First arg
	; [ebp + 12] -> Second arg
	
	mov edx, [ebp + 8]  ; edx = 'x' 
	mov ecx, [ebp + 12] ; ecx = 'n'
	xor eax, eax		; Zeroes eax register, eax = sum

	cmp ecx, 0
	jle InvalidCount 

@@:	add eax, [edx]		; Add next element to sum.
	add edx, 4			; Points to next element.

	dec ecx				; Adjust counter.
	jnz @B				; Jump backward to the next @@ label if not equal to zero.

InvalidCount:
	pop ebp				; Epilogue.
	ret

CalcArraySumASM endp
	end