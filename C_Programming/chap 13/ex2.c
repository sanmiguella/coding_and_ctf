#include <stdio.h>
#include <string.h>

int main()
{
    char c;

    printf("Would you like your computer to explode? "); 
    c = getchar();

    if(c == 'N')
    {
        printf("\nOkay! Whew!\n");  
    }

    else
    {
        printf("\nOK: Configuring computer to explode now.\n");
        printf("\nBye!\n");
    }

    return(0);
}
