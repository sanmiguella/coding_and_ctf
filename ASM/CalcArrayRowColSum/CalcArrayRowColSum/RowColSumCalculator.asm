.model flat, c
.code

CalcArrayRowColSum proc
	; Prologue
	push ebp 
	mov	ebp, esp 

	; Saving registers. 
	push ebx 
	push esi 
	push edi 

	; Initializing register values. 
	xor ebx, ebx						; Zeroes ebx register.
	xor esi, esi						; Zeroes esi register.
	xor edi, edi						; Zeroes edi register.

	cmp dword ptr [ebp + 12], 0			; [ebp + 12] = 'nRows', compares nRows to 0.
	jle InvalidArg						; If nRows <= 0, terminate

	mov ecx, [ebp + 16]					; [ebp + 16] = 'nCols'
	cmp ecx, 0							; Compares nCols to 0.
	jle	InvalidArg						; If nCols <= 0, terminate

	mov edi, [ebp + 24]					; edi = 'col_sums'
	xor eax, eax						; Zeroes eax register.
	rep stosd							; Fill array with zeros

	mov ebx, [ebp + 8]					; ebx = 'x'
	xor esi, esi						; i = 0
	
; int CalcArrayRowColSum(const int* x, int nRows, int nCols, int* row_sums, int* col_sums)				
; conts int* x	= ebp + 8
; int nRows		= ebp + 12
; int nCols		= ebp + 16
; int* row_sums = ebp + 20
; int* col_sums = ebp + 24

loop_outer:								; Outer loop.

	mov edi, [ebp + 20]					; edi = *row_sums
	mov dword ptr [edi + esi * 4], 0	; row_sums[i] = 0
	xor edi, edi						; j = 0, inner loop
	mov edx, esi						; edx = i
	imul edx, [ebp + 16]				; edx = i * nCols

loop_inner:								; Inner loop.

	mov ecx, edx						; ecx = (i * nCols)
	add ecx, edi						; ecx = (i * nCols) + j
	mov	eax, [ebx + ecx * 4]			; eax =	x[ (i * nCols + j) ] 
	
	mov ecx, [ebp + 20]					; ecx = 'row_sums' 
	add[ecx + esi * 4], eax				; row_sums[i] += eax
	
	mov ecx, [ebp + 24]					; ecx = col_sums
	add[ecx + edi * 4], eax				; col_sums[j] += eax

	inc edi								; j++
	cmp edi, [ebp + 16]					; Compare j and nCols
	jl loop_inner						; jump if (j < nCols)

	inc esi								; i++
	cmp esi, [ebp + 12]					; Compare i with nRows
	jl loop_outer						; Loop if i < nRows
	mov eax, 1

InvalidArg:

	pop edi
	pop esi
	pop ebx
	pop ebp
	ret

CalcArrayRowColSum endp
	end