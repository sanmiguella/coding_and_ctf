#include <stdio.h>
#include <string.h>

/* To compile:
    gcc -fno-stack-protector -zexecstack vuln.c -o vuln
*/

void overflow() {
    char buffer[128];

    printf("Input -> "); 
    gets(buffer);    
    
    printf("You entered -> %s\n", buffer);
}

int main() {
    overflow();
    
    return(0);
}
