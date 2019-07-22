.model flat, c
.code

CountChar proc 
	; Prologue.
	push ebp 
	mov ebp, esp
	
	; Saving register. 
	push esi 

	xor edx, edx		; Zero-es edx, edx = occurence counter = found.
	xor ecx, ecx		; Zero-es ecx.

	; CountChar(wchar_t *s, wchar_t c)
	mov esi, [ebp + 8]	; esi = 's'
	mov cx,	[ebp + 12]	; cx = 'c'
	
	; lodsw : Load String word from Data segment(DS): edi/esi to register ax, then increment esi by 2.
	; Increment by 2 : Points to the next word
	; Word  : 16 bit -> 2 Bytes
	; Dword : 32 bit -> 4 Bytes

; @@B
@@:	lodsw				; Load next char into ax 
	or ax, ax			; Test for end of string. 
	jz @F				; If ax == '\x00', jump forward.

	cmp ax, cx			; Compare current character(ax) with the character we are looking for(cx).
	jne @B				; If char(index) != end of string, jump backwards. 
	inc edx				; If Match == True, found++; 
	jmp @B				; After `Match` is incremented, jump backwards.

; @@F
@@: mov eax, edx		; eax = characther count

	; Epilogue.
	pop esi
	pop ebp
	ret

CountChar endp
	end


