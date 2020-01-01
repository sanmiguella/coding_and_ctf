.model flat, c

.code
CopyStrAsm proc 
	; Prologue
	push ebp 
	mov ebp, esp 

	; Save reg values.
	push esi
	push edi 
	push ebx

	; CopyStrAsm(char *msg, char *copy, int msg_size)
	xor eax, eax 
	xor ebx, ebx			; ebx = index

	; Load argument
	mov esi, [ebp + 8]		; esi = msg
	mov edi, [ebp + 12]		; edi = copy
	mov ecx, [ebp + 16]		; ecx = msg_size

@@: mov al, [esi + ebx]		; al = msg[index] 
	mov [edi + ebx], al		; copy[index] = al 
	add ebx, 1				; index++ : move to the next byte, 1 char = 1 byte

	cmp ebx, ecx			; Check if index == msg_size		
	jl @B					; Jump if index < msg_size 

	; Restore reg values.
	pop ebx
	pop edi
	pop esi 

	; Epilogue
	pop ebp
	ret
	
CopyStrAsm endp
	end