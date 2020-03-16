#include <stdio.h>
#define BUF_SIZE 64
   
int main(void)
{
    char kitty[BUF_SIZE]; 
    
    printf("What would you like to name your cat? "); 
    gets(kitty);

    printf("%s is a nice name, What else do you have in mind? ", kitty); 
    gets(kitty);
    
    printf("%s is nice. too.\n", kitty);
    return(0); 
}
