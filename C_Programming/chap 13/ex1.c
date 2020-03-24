#include <stdio.h>
#include <stdlib.h>


int main()
{
    char a, b; 

    printf("Which character is greater?\n");

    printf("\nType a single character: ");
    scanf("%c", &a); 

    fflush(stdin);
    printf("\nType another character: "); 
    scanf("%c", &b); 

    if(a > b)
    {
        printf("\n\n%c is greater than %c!\n", a, b);
    }

    else if(b > a)
    {
        printf("\n\n%c is greater than %c!\n", b, a);
    }

    else 
    {
        printf("\n\nNext time, don't type the same char twice\n");
    }

    return(0);
}
