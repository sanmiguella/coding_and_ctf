#include <stdio.h>
#define SMALL_SIZE 32

int main(void)
{
    char name[SMALL_SIZE]; 
    char color[SMALL_SIZE]; 

    printf("%15s", "");
    printf("What is your name? "); 
    scanf("%s", name); 

    printf("%15s", "");
    printf("What is your favorite color? "); 
    scanf("%s", color); 

    printf("%15s", "");
    printf("%s's favorite color is %s !!\n", name, color); 

    return(0);
}
