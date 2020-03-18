#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char shellcode[] = \
		   "\xeb\x19\x31\xc0\x31\xdb\x31\xc9\x31\xd2\xb0\x04\xb3\x01\x59\xb2\x08\xcd\x80\x31\xc0\xb0\x01\x31\xdb\xcd\x80\xe8\xe2\xff\xff\xff\x2f\x62\x69\x6e\x2f\x73\x68\x0a";

int main(int argc, char **argv)
{
	printf("Shellcode Length: %d Bytes\n", strlen(shellcode));

	int (*ret)(); // ret is a function pointer
	ret = (int(*)())shellcode; // ret points to shellcode

	(int)(*ret)();	// execute as function shellcode[]
	//exit(0);
}
