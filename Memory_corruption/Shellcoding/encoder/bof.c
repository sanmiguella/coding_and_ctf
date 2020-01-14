#include <stdio.h>
#include <string.h>

void overflow(char *src)
{
    char dest[256];

    strcpy(dest, src);
    printf("[+] You entered : %s\n", dest);
}

int main(int argc, char *argv[]) 
{
    if (argc > 1) {
       overflow(argv[1]); 
    } 
    else {
       printf("[!] You did not enter any data...\n");
    }
}
