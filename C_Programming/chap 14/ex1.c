#include <stdio.h>

int main()
{
    char c;
    
    printf("Would you like your computer to explode? ");
    c = getchar(); 

    if(c == 'Y' || c == 'y')
    {
        printf("\nOK: Configuring computer to explode now.\n");
        printf("Bye!\n");
    }
    
    else
    {
        printf("\nOkay. Whew!\n");
    }

    return(0);
}
