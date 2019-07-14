.386
.model flat, c

	extern GlChar:byte 
	extern GlShort:word 
	extern GlInt:dword
	extern GLongLong:qword 

	.code

IntegerAddition proc
	push ebp
	mov ebp, esp

; IntegerAddition(char a, short b, int c, long long d)
; ebp + 8 : a
; ebp + 12 : b
; ebp + 16 : c
; ebp + 20 : d

; Compute GLChar += a
	mov al,[ebp + 8]
	add [GlChar],al

; Compute GlShort += b
	mov ax,[ebp + 12]
	add [GlShort],ax 

; Compute GlInt += c
	mov eax,[ebp + 16] 
	add [GlInt],eax 

; Compute GLongLong += c
; GLongLong is 64bit but right now we are doing this on 32 bit.
	mov eax,[ebp + 20] 
	mov edx,[ebp + 24] 
	add dword ptr[GLongLong],eax 
	adc dword ptr[GLongLong],edx 

	pop ebp
	ret

IntegerAddition endp
	end