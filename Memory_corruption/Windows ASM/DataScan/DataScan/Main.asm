.386
.model flat 

.data 
;intArray SWORD 0,0,0,0,4,3,0,-34,-56,7,8
intArray SWORD 0,0,0,0,0,0,0,0,0,0

.code
main proc 
	mov ebx, OFFSET intArray ; address of intArray to ebx. 
	mov ecx, LENGTHOF intArray ; initialize the loop counter.

L1:
	cmp WORD PTR[ebx], 0 ; compare the data inside the pointer to 0.
	jnz found ; jump to label found if value is not zero.
	add ebx, 2 ; go into the next element.
	loop L1 
	jmp notFound

found:
	movsx eax, WORD PTR[ebx]
	jmp quit

notFound:
	mov eax, 99999999h

quit:
	ret 

main endp
end main
