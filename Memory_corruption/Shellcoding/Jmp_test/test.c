#include <stdio.h>
#include <string.h>

unsigned char code[] = \
"\xeb\x19\x31\xc0\x31\xdb\xb0\x04\xb3\x01\x8b\x0c\x24\xb2\x0b\xcd\x80\x31\xc0\x31\xdb\xb0\x01\xb3\xff\xcd\x80\xe8\xe2\xff\xff\xff\x2f\x65\x74\x63\x2f\x70\x61\x73\x73\x77\x64";

main() {
    printf("shellcode length : %d\n", strlen(code)); 
    int (*ret)() = (int(*)())code; 
    ret();
}
