.386
.model flat, stdcall
.stack 4096
ExitProcess proto, dwExitcode: dword

.data 
; 1 word : 2 bytes
; 2 words : Dword : 4 bytes
; 4 words : Qword : 8 bytes


first_val dword 20002000h 
second_val dword 11111111h
third_val dword 22222222h 
sum dword 0

.code 
main proc 
	xor eax, eax

	mov eax, first_val		; eax = 2000 2000
	add eax, second_val		; eax = 3111 3111
	add eax, third_val		; eax = 5333 5333

	mov sum, eax			; sum = 5333 5333

	invoke ExitProcess, 0 
main endp 
end main