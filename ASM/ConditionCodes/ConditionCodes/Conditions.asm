.model flat, c
.code 


SignedMinA proc			; Find minA()
	push ebp			; Prologue
	mov ebp, esp

	mov eax, [ebp + 8]	; eax = 'a' 
	mov ecx, [ebp + 12] ; ecx = 'b'
	
	cmp eax, ecx 
	jle @F				; jump to nearest @@ if less than or equal to
	mov eax, ecx		; eax = min(a, b)		

@@:	mov ecx, [ebp + 16]	; ecx = 'c'
	cmp eax, ecx
	jle @F
	mov eax, ecx		; eax = min(a, b, c)

@@: pop ebp 			; Epilogue
	ret
SignedMinA endp


SignedMaxA proc			; Find maxA()
	push ebp			; Prologue
	mov ebp, esp

	mov eax, [ebp + 8]	; eax = 'a'
	mov ecx, [ebp + 12]	; ecx = 'b'

	cmp eax, ecx 
	jge @F				; jump to nearest @@ if greater than or equal to
	mov eax, ecx		; eax = max(a, b)

@@: mov ecx, [ebp + 16] ; ecx = 'c'
	cmp eax, ecx
	jge @F				; eax = max(a, b, c)
	mov eax, ecx		; eax = max(a, b, c)

@@: pop ebp				; Epilogue
	ret
SignedMaxA endp


SignedMinB proc			; Find minB()
	push ebp			; Prologue
	mov ebp, esp		

	mov eax, [ebp + 8]	; eax = 'a' 
	mov ecx, [ebp + 12] ; ecx = 'b' 

	cmp eax, ecx
	cmovg eax, ecx		; Copies the content of 'ecx to eax' if 'eax is greater than ecx', min(a, b)

	mov ecx, [ebp + 16] ; ecx = 'c'
	cmovg eax, ecx		; eax = min(a, b, c)

	pop ebp				; Epilogue
	ret
SignedMinB endp


SignedMaxB proc			; Find maxB()
	push ebp			; Prologue
	mov ebp, esp 

	mov eax, [ebp + 8]	; eax = 'a' 
	mov ecx, [ebp + 12] ; ecx = 'b' 
	
	cmp eax, ecx
	cmovl eax, ecx		; Copies the content of 'ecx to eax' if 'eax is lesser than ecx', max(a, b)

	mov ecx, [ebp + 16]	; ecx = 'c'
	cmovl eax, ecx		; eax = max(a, b, c)

	pop ebp				; Epilogue
	ret
SignedMaxB endp

end