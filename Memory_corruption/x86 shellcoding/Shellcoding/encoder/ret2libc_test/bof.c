#include <stdio.h>
#include <string.h>

void overflow(char *src)
{
    char buf[256];

    strcpy(buf, src);
    printf("\n[+] You entered : %s\n", buf);
}

int main()
{
    char buf[512]; 
    
    printf("[+] Please enter data :\n"); 
    gets(buf); 

    overflow(buf);

    return 0;
}
