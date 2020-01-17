#include <stdio.h>

void overflow();

int main()
{
    overflow();

    return 0;
}

void overflow()
{
    char buf[512];

    printf("[+] Please enter data : ");
    gets(buf);

    printf("\n[+] You entered : %s\n", buf);
}
