.386
.model flat, c
.code

calculate_sum proc

	; Function prologue
	push ebp
	mov	 ebp, esp 

	; Allocates 12 byte of local storage on the stack that can be used by the function
	; X86 stack grows downwards towards lower memory address
	sub esp, 12 
	
	; Saves non-volatile registers
	push ebx 
	push esi
	push edi

	; Function arguments are always referenced using positive displacement values
	; Local variables are always referenced using negative displacement values

	; Load arguments
	mov eax, [ebp +8]  ; eax = 'a'
	mov ebx, [ebp +12] ; ebx = 'b'
	mov ecx, [ebp +16] ; ecx = 'c'
	mov edx, [ebp +20] ; edx = 's1'
	mov esi, [ebp +24] ; esi = 's2' 
	mov edi, [ebp +28] ; edi = 's3' 

	; Adds the sum of 'a', 'b', 'c' into [ebp -12] : Temp 's1' 
	; [ebp -12] : Temp 's1' -> 'a' + 'b' + 'c' 
	mov [ebp -12], eax ; Moves eax 'a' into [ebp -12] 
	add [ebp -12], ebx ; Adds 'b' to 'a' 
	add [ebp -12], ecx ; Adds 'c' to 'a'

	; Multiply the content of a register and store the result in the said register
	; 's2' = ('a' * 'a') + ('b' * 'b') + ('c' * 'c')
	imul eax, eax ; 'a' = 'a' * 'a' 
	imul ebx, ebx ; 'b' = 'b' * 'b' 
	imul ecx, ecx ; 'c' = 'c' * 'c'	
	mov [ebp -8], eax ; Stores the value of 'a' to 's2' : [ebp -8] 
	add [ebp -8], ebx ; Adds 'b' to 'a'
	add [ebp -8], ecx ; Adds 'c' to 'a'

	; 's3' = ('a' * 'a' * 'a') + ('b' * 'b' * 'b') + ('c' * 'c' * 'c')
	imul eax, [ebp +8]  ; 'a' * 'a' * 'a'
	imul ebx, [ebp +12] ; 'b' * 'b' * 'b'
	imul ecx, [ebp +16] ; 'c' * 'c' * 'c'
	mov [ebp -4], eax ; Stores the value of eax 'a' to 's3' : [ebp -4]
	add [ebp -4], ebx ; Adds 'b' to 'a' 
	add [ebp -4], ecx ; Adds 'c' to 'a'

	; Saves 's1', 's2', 's3'
	mov eax, [ebp -12] ; Stores the value of temp 's1' to eax
	mov [edx], eax ; Stores the value of temp 's1' to 's1'

	mov eax, [ebp -8] ; Stores the value of temp 's2' to eax
	mov [esi], eax ; Stores the value of temp 's2' to 's2'

	mov eax, [ebp -4] ; Stores the value of temp 's3' to eax 
	mov [edi], eax ; Stores the value of temp 's3' to 's3'

	; Function epilogue

	; Restores Non-volatile register
	pop edi
	pop esi
	pop ebx
	
	; Release previously allocated stack space, restore esp to the correct value before execution of ret
	mov esp, ebp 
	pop ebp 
	ret

calculate_sum endp
end