#include <stdio.h>

void overflow();

int main(void)
{
    overflow(); 
    return(0);
}

void overflow()
{
    char buffer[128]; 

    printf("Input? -> "); 
    gets(buffer); 

    printf("Output? -> %s\n", buffer); 
}
