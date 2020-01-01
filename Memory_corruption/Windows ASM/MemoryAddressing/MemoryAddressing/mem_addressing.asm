.386 
.model flat, c

; Simple lookup table (.const section data is read only)

.const
FibVals	dword 0	, 1, 1, 2, 3, 5, 8, 13 
		dword 21, 34, 55, 89, 144, 233, 377, 610

; 1 word				: 2 bytes
; 2 words(double word)	: 4 bytes
; 4 words(quad word)	: 8 bytes

NumFibVals dword ($ - FibVals) / sizeof dword 
public NumFibVals

; extern "C" int MemoryAddressing(int i, int* v1, int* v2, int* v3, int *v4)
; Return code: 0 -> Error(invalid table index)
;			 : 1 -> Success
;
; [ebp + 8] =  i
; [ebp + 12] = *v1 
; [ebp + 16] = *v2
; [ebp + 20] = *v3 
; [ebp + 24] = *v4

.code 

MemoryAddressing proc
	; Function Prologue. 
	push ebp 
	mov ebp, esp 

	; Saving of non-volatile registers. 
	push ebx 
	push esi 
	push edi 

	; Make sure 'i' is valid 
	; ecx = program counter
	xor eax, eax			; eax = 0
	mov ecx, [ebp + 8]		; ecx = i 

	cmp ecx, 0				; compare ecx to 0
	jl  Invalid_index		; jump to Invalid_index if ecx < 0
	
	cmp ecx, [NumFibVals]	; compare ecx to NumFibVals
	jge Invalid_index		; jump to Invalid_index if ecx >= NumFibVals
	

	; Example #1 - base register 
	mov ebx, offset FibVals	; ebx = FibVals
	mov esi, [ebp + 8]		; esi = i
	shl esi, 2				; esi = i * 4
	add ebx, esi			; ebx = FibVals + (i * 4)
	mov eax, [ebx]			; eax = FibVals + (i * 4)
	mov edi, [ebp + 12]		; edi = *v1 
	mov [edi], eax			; *v1 = FibVals + (i * 4)

	; Example #2 - base register + displacement
	; esi is used as the base register 
	mov esi, [ebp + 8]			; esi = i 
	shl esi, 2					; esi = i * 4
	mov eax, [esi + FibVals]	; eax = (i * 4) + FibVals
	mov edi, [ebp + 16]			; edi = *v2 
	mov [edi], eax				; *v2 = (i * 4) + FibVals

	; Example #3 - base register + index register
	mov ebx, offset FibVals		; ebx = FibVals
	mov esi, [ebp + 8]			; esi = i
	shl esi, 2					; esi = i * 4
	mov eax, [ebx + esi]		; eax = FibVals + (i * 4)
	mov edi, [ebp + 20]			; edi = *v3
	mov [edi], eax				; *v3 = FibVals + (i * 4)
	
	; Example #4 - base register + index register * scale factor
	mov ebx, offset FibVals		; ebx = FibVals
	mov esi, [ebp + 8]			; esi = i 
	mov eax, [ebx + esi * 4]	; eax = FibVals + i * 4
	mov edi, [ebp + 24]			; edi = *v4
	mov [edi], eax				; *v4 = FibVals + i * 4
	
	mov eax, 1					; Set success return code.

Invalid_index: 
	pop edi
	pop esi 
	pop ebx 
	pop ebp
	ret 

MemoryAddressing endp
	end	