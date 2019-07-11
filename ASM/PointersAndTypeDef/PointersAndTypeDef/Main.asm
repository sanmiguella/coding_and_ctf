.386
.model flat

PBYTE TYPEDEF PTR BYTE ; pointer to a byte
PWORD TYPEDEF PTR WORD ; pointer to PWORD
PDWORD TYPEDEF PTR DWORD ; pointer to PDWORD

.data
arrayB BYTE 10h, 20h, 30h
arrayW WORD 1, 2, 3
arrayD DWORD 4, 5, 6

pt_1 PBYTE arrayB ; pointer to address of arrayB
pt_2 PWORD arrayW ; pointer to address of arrayW
pt_3 PDWORD arrayD ; pointer to address of arrayD

.code 
start PROC
	mov esi, pt_1		; esi: address to an array with 1 byte elements
	mov al, [esi]		; 0xdeadbe10, lower 8 bits, 1 byte
	mov al, [esi + 1]	; 0xdeadbe20, lower 8 bits, 1 byte
	mov al, [esi + 2]	; 0xdeadbe30, lower 8 bits, 1 byte

	mov esi, pt_2		; esi: address to an array with 2 byte elements
	mov ax, [esi]		; 0xdead0001, lower 16 bits, 2 byte
	mov ax, [esi + 2]	; 0xdead0002, lower 16 bits, 2 byte
	mov ax, [esi + 4]	; 0xdead0003, lower 16 bits, 2 byte

	mov esi, pt_3		; esi: address to an array with 4 byte elements
	mov eax, [esi]		; 0x00000004, 32 bits, 4 byte
	mov eax, [esi + 4]	; 0x00000005, 32 bits, 4 byte
	mov eax, [esi + 8]	; 0x00000006, 32 bits, 4 byte

	ret
start endp 
end start