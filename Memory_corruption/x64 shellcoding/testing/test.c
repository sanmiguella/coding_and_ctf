#include <stdio.h>
#include <string.h>

unsigned char code[] = \
"\x48\x31\xc0\xb0\x01\x48\x31\xdb\xb3\x02\x48\x31\xc9\xb1\x03\x48\x31\xd2\xb2\x04\xb0\x3c\x48\x31\xff\x66\xbf\xff\xff\x0f\x05";

int main()
{
    printf("Shellcode Length:  %d\n", strlen(code));

    int (*ret)() = (int(*)())code;

    ret();
}