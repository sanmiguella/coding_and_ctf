.model flat, c
.code

CalcArraySquaresASM proc
	push ebp
	mov ebp, esp	; Prologue

	push ebx 
	push esi 
	push edi 

	; Load argument
	mov edi, [ebp + 8]	; 1st arg: y[]
	mov esi, [ebp + 12]	; 2nd arg: x[]
	mov ecx, [ebp + 16] ; 3rd arg: n

	xor eax, eax	; Zeroes the register. eax = sum of 'y' array 
	cmp ecx, 0 
	jle EmptyArray
	
	shl ecx, 2		; ecx = size of array in bytes 
	xor ebx, ebx	; ebx = array element offset

@@:	mov edx, [esi + ebx]	; Load next x[i] 
	imul edx, edx			; x * x
	mov [edi + ebx], edx	; Saves result to y[i]
	add eax, edx			; sum += x[i] * x[i]
	add ebx, 4				; Update array element offset.
	cmp ebx, ecx
	jl @B					; If ebx is not equals to ecx, keeps looping.

EmptyArray:
	pop edi
	pop esi
	pop ebx
	pop ebp
	ret
CalcArraySquaresASM endp
	end