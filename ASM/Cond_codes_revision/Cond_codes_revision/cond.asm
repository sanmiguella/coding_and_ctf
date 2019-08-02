.386
.model flat, c
.code

; extern "C" int SignedMaxA_asm(int a, int b, int c);
SignedMaxA_asm proc	

	; Prologue
	push ebp 
	mov ebp, esp
	
	; [ebp + 8] = 'a'
	; [ebp + 12] = 'b'
	; [ebp + 16] = 'c'
	mov eax, [ebp + 8]		; eax = 'a'
	mov ecx, [ebp + 12]		; ecx = 'b'

	cmp eax, ecx			; Compare 'a' with 'b' 
	jge @F					; Jump Forward if 'a' > 'b'
	mov eax, ecx			; IF 'b' > 'a' THEN eax = 'b'

	@@:
	mov ecx, [ebp + 16]		; ecx = 'c'
	cmp eax, ecx			; Compare max(a, b) with 'c'
	jge @F					; Jump Forward if max(a, b) > 'c'
	mov eax, ecx			; IF 'c' > max(a, b) THEN eax = 'c'

	@@:
	pop ebp
	ret

SignedMaxA_asm endp
	end